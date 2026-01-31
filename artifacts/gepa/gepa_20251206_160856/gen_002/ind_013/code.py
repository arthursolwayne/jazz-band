
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time in seconds per bar (160 BPM, 4/4 time)
bar_length = 6.0 / 4  # 1.5 seconds per bar
beat_length = bar_length / 4  # 0.375 seconds per beat

# Helper function to create a note
def note_on(note_number, time, duration, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + duration)
    return note

# Helper function to create a rhythm (note on beats)
def rhythm_beats(note_number, start_time, beat_indices, duration, velocity=100):
    notes = []
    for beat in beat_indices:
        time = start_time + beat * beat_length
        note = note_on(note_number, time, duration, velocity)
        notes.append(note)
    return notes

# --- DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4):
    start_time = bar * bar_length
    # Kick on beats 0 and 2
    kicks = rhythm_beats(36, start_time, [0, 2], 0.15, velocity=80)
    # Snare on beats 1 and 3
    snares = rhythm_beats(38, start_time, [1, 3], 0.15, velocity=85)
    # Hi-hat on every eighth
    hihat_notes = []
    for i in range(8):
        time = start_time + i * beat_length / 2
        hihat_notes.append(note_on(56, time, 0.1, velocity=60))
    # Add to drums
    drums.notes.extend(kicks)
    drums.notes.extend(snares)
    drums.notes.extend(hihat_notes)

# --- BASS: Marcus
# Walking bass, roots and fifths with chromatic approaches
# Bar 1: root (F), 5th (C), chromatic (B), root (F)
for bar in range(4):
    start_time = bar * bar_length
    if bar == 0:
        notes = [
            note_on(71, start_time, 0.375),  # F
            note_on(76, start_time + 0.375, 0.375),  # C
            note_on(75, start_time + 0.75, 0.375),  # B (chromatic)
            note_on(71, start_time + 1.125, 0.375),  # F
        ]
    elif bar == 1:
        notes = [
            note_on(71, start_time, 0.375),  # F
            note_on(76, start_time + 0.375, 0.375),  # C
            note_on(77, start_time + 0.75, 0.375),  # C#
            note_on(71, start_time + 1.125, 0.375),  # F
        ]
    elif bar == 2:
        notes = [
            note_on(71, start_time, 0.375),  # F
            note_on(76, start_time + 0.375, 0.375),  # C
            note_on(74, start_time + 0.75, 0.375),  # Bb (chromatic)
            note_on(71, start_time + 1.125, 0.375),  # F
        ]
    elif bar == 3:
        notes = [
            note_on(71, start_time, 0.375),  # F
            note_on(76, start_time + 0.375, 0.375),  # C
            note_on(76, start_time + 0.75, 0.375),  # C
            note_on(71, start_time + 1.125, 0.375),  # F
        ]
    bass.notes.extend(notes)

# --- PIANO: Diane
# Open voicings, different chords per bar, comp on 2 and 4
# Bar 1: F7 (F A C Eb)
# Bar 2: Fm7 (F Ab Bb C)
# Bar 3: Fmaj7 (F A C E)
# Bar 4: F7 again with variation
for bar in range(4):
    start_time = bar * bar_length
    if bar == 0:
        # F7: F, A, C, Eb
        chord_notes = [71, 74, 76, 70]
    elif bar == 1:
        # Fm7: F, Ab, Bb, C
        chord_notes = [71, 69, 71, 76]
    elif bar == 2:
        # Fmaj7: F, A, C, E
        chord_notes = [71, 74, 76, 79]
    elif bar == 3:
        # F7 variation: F, A, C, Eb (with a slight chromatic run)
        chord_notes = [71, 74, 76, 70]
    # Comp on beats 2 and 4
    for i, note in enumerate(chord_notes):
        time = start_time + (i * beat_length)
        duration = 0.375
        piano.notes.append(note_on(note, time, duration, velocity=90))

# --- SAX: Dante
# Motif: F, G, F#, E (sings like a question)
# Bar 1: start the motif (F, G, F#, E)
# Bar 2: rest
# Bar 3: continue the motif (F, G, F#, E)
# Bar 4: rest and resolution

# Bar 1: motif
notes = [
    note_on(71, 0, 0.375, velocity=110),  # F
    note_on(72, 0.375, 0.375, velocity=110),  # G
    note_on(73, 0.75, 0.375, velocity=110),  # F#
    note_on(71, 1.125, 0.375, velocity=110),  # E
]
sax.notes.extend(notes)

# Bar 3: repeat motif with slight variation (same notes, slightly lower velocity)
notes = [
    note_on(71, 3 * bar_length, 0.375, velocity=105),  # F
    note_on(72, 3 * bar_length + 0.375, 0.375, velocity=105),  # G
    note_on(73, 3 * bar_length + 0.75, 0.375, velocity=105),  # F#
    note_on(71, 3 * bar_length + 1.125, 0.375, velocity=105),  # E
]
sax.notes.extend(notes)

# Write the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
