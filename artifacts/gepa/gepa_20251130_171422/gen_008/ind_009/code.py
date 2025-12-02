
import pretty_midi

# Set up MIDI
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # 480 ticks per quarter note

# Set tempo (160 BPM)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0, cues=0)]
pm.tempos = [pretty_midi.TempoChange(tempos=160.0, time=0)]

# Define time per bar (in seconds)
BAR_LENGTH = 1.5
TICKS_PER_BAR = pm.resolution * BAR_LENGTH * pm.tempos[0].tempos[0] / 60.0

# Define instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Fingerstyle Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Define note values in ticks
def note_to_ticks(duration):
    return int(duration * pm.resolution / 60.0 * 160.0)

# Define note functions
def create_note(note_number, start_tick, duration_ticks):
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start_tick, end=start_tick + duration_ticks)
    return note

# Define time increments for each bar
def bar_to_tick(bar):
    return int(bar * TICKS_PER_BAR)

# =============== DRUMS ===============
# Kick on 1 and 3
# Snare on 2 and 4
# Hi-hat on every eighth (2 per beat)

for bar in range(4):
    beat_start = bar_to_tick(bar)

    # Kick on beat 1 and 3
    for beat in [0, 2]:
        kick_start = beat_start + beat * (TICKS_PER_BAR / 4)
        drums.notes.append(create_note(36, kick_start, note_to_ticks(0.25)))

    # Snare on beat 2 and 4
    for beat in [1, 3]:
        snare_start = beat_start + beat * (TICKS_PER_BAR / 4)
        drums.notes.append(create_note(38, snare_start, note_to_ticks(0.25)))

    # Hi-hat on every eighth note
    for eighth in range(8):
        hihat_start = beat_start + eighth * (TICKS_PER_BAR / 8)
        drums.notes.append(create_note(42, hihat_start, note_to_ticks(0.125)))

# =============== BASS LINE (Marcus) ===============
# Chromatic walking line in D major
# D -> C# -> E -> F -> E -> F# -> G -> A -> G -> A -> B -> C -> B -> C# -> D
# D (beat 1), C# (beat 2), E (beat 3), F (beat 4), E (beat 1), F# (beat 2), G (beat 3), A (beat 4), etc.

bass_notes = [
    (62, 0),     # D
    (61, 1),     # C#
    (64, 2),     # E
    (65, 3),     # F
    (64, 4),     # E
    (66, 5),     # F#
    (67, 6),     # G
    (69, 7),     # A
    (67, 8),     # G
    (69, 9),     # A
    (71, 10),    # B
    (72, 11),    # C
    (71, 12),    # B
    (72, 13),    # C
    (73, 14),    # C#
    (62, 15)     # D
]

for note, beat in bass_notes:
    start_tick = bar_to_tick(beat // 4) + (beat % 4) * (TICKS_PER_BAR / 4)
    bass.notes.append(create_note(note, start_tick, note_to_ticks(0.25)))

# =============== PIANO (Diane) ===============
# Comping on 2 and 4 with 7th chords, some chromatic movement
# D7 -> G7 -> C7 -> A7 (with chromatic notes)

piano_notes = [
    (72, 0, 2),   # C (from D7)
    (74, 0, 2),   # E (from D7)
    (76, 0, 2),   # G (from D7)
    (79, 0, 2),   # B (from D7)
    (79, 1, 2),   # B (from G7)
    (81, 1, 2),   # D (from G7)
    (83, 1, 2),   # F# (from G7)
    (86, 1, 2),   # A (from G7)
    (72, 2, 2),   # C (from C7)
    (74, 2, 2),   # E (from C7)
    (77, 2, 2),   # G (from C7)
    (79, 2, 2),   # B (from C7)
    (79, 3, 2),   # B (from A7)
    (82, 3, 2),   # C# (chromatic)
    (84, 3, 2),   # E (from A7)
    (86, 3, 2)    # A (from A7)
]

for note, bar, beat in piano_notes:
    start_tick = bar_to_tick(bar) + beat * (TICKS_PER_BAR / 4)
    piano.notes.append(create_note(note, start_tick, note_to_ticks(0.25)))

# =============== SAX (You) ===============
# Motif: D -> F -> G -> B (4 notes), then rest for 2 bars, repeat in bar 4
# D (beat 1 of bar 1), F (beat 2 of bar 1), G (beat 3 of bar 1), B (beat 4 of bar 1)

sax_notes = [
    (62, 0, 0),   # D
    (65, 0, 1),   # F
    (67, 0, 2),   # G
    (71, 0, 3),   # B
    (62, 3, 0),   # D (repeat in bar 4)
]

for note, bar, beat in sax_notes:
    start_tick = bar_to_tick(bar) + beat * (TICKS_PER_BAR / 4)
    sax.notes.append(create_note(note, start_tick, note_to_ticks(0.25)))

# Save the MIDI file
pm.write('jazz_intro_4bars.mid')

print("MIDI file written as 'jazz_intro_4bars.mid'")
