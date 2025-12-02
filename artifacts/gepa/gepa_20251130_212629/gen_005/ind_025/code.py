
import pretty_midi

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define the key (D major)
key = 'D'

# Define time in seconds per bar (BPM = 160, 1 bar = 60 / 160 * 4 = 1.5s)
bar_length = 1.5

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
bass_program = pretty_midi.instrument_name_to_program('Electric Bass (Finger)')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drum = pretty_midi.Instrument(program=drum_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum, bass, piano, sax]

# =====================
# Bar 1: Little Ray (drums)
# =====================

# Kick on 1 and 3 (Bar 1)
kick_on = [0.0, 0.75]
for kick_offset in kick_on:
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_offset, end=kick_offset + 0.1)
    drum.notes.append(kick_note)

# Snare on 2 and 4 (Bar 1)
snare_on = [0.375, 1.125]
for snare_offset in snare_on:
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_offset, end=snare_offset + 0.1)
    drum.notes.append(snare_note)

# Hi-hat on every eighth (Bar 1)
hihat_on = [0.0, 0.375, 0.75, 1.125, 1.5]
for hihat_offset in hihat_on:
    hihat_note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_offset, end=hihat_offset + 0.05)
    drum.notes.append(hihat_note)

# =====================
# Bars 2–4: Full Ensemble
# =====================

# Define the start time for bars 2–4
start_time = 1.5

# Bass line: Walking line in D major
bass_notes = [
    (38, start_time + 0.0),   # D (root)
    (40, start_time + 0.25),  # E
    (42, start_time + 0.5),   # F#
    (43, start_time + 0.75),  # G
    (47, start_time + 1.0),   # B
    (45, start_time + 1.25),  # A
    (42, start_time + 1.5),   # F#
    (40, start_time + 1.75),  # E
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# D7 on beat 2, A7 on beat 4, both bars
piano_notes = [
    # Bar 2: D7 on beat 2 (time = start_time + 0.375)
    (2, start_time + 0.375),   # D
    (4, start_time + 0.375),   # F#
    (7, start_time + 0.375),   # A
    (10, start_time + 0.375),  # C#
    # Bar 3: A7 on beat 4 (time = start_time + 1.125)
    (10, start_time + 1.125),  # A
    (13, start_time + 1.125),  # C#
    (15, start_time + 1.125),  # E
    (17, start_time + 1.125),  # G
    # Bar 4: D7 on beat 2 (time = start_time + 1.375)
    (2, start_time + 1.375),   # D
    (4, start_time + 1.375),   # F#
    (7, start_time + 1.375),   # A
    (10, start_time + 1.375),  # C#
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Tenor Sax: Short, melodic motif. Simple, with space.
# The motif: D (start) -> E -> D (return) -> question on G
# SX: D, E, D, G
sax_notes = [
    (2, start_time + 0.0),    # D
    (4, start_time + 0.25),   # E
    (2, start_time + 0.5),    # D
    (7, start_time + 0.75),   # G
    (2, start_time + 1.0),    # D
    (4, start_time + 1.25),   # E
    (2, start_time + 1.5),    # D
    (7, start_time + 1.75),   # G
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Save the MIDI file
pm.write('wayne_shorter_intro.mid')
print("MIDI file saved as 'wayne_shorter_intro.mid'")
