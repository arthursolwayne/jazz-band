
import pretty_midi

# Create a PrettyMIDI object with 160 BPM and 4/4 time
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: Dm (D minor)
key = 'Dm'

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define the tempo
pm.tempos = [pretty_midi.TempoChange(tempo=160, time=0.0)]

# Define the note durations in seconds
beat = 0.375  # 60 / 160
bar = 1.5  # 4 beats per bar

# ---------------------------
# Bar 1 - Little Ray (Drums)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Build tension with rhythm, not sound

drum_program = pretty_midi.instrument_program('架子鼓')  # 'Drum Kit' in Chinese
drum_inst = pretty_midi.Instrument(program=drum_program)

# Kick on 1 and 3
kick_notes = [pretty_midi.note_number_to_name(36)]  # C1
kick_times = [0.0, beat * 2.0]

# Snare on 2 and 4
snare_notes = [pretty_midi.note_number_to_name(62)]  # G3
snare_times = [beat * 1.0, beat * 3.0]

# Hihat on every eighth note (8 hits per bar)
hihat_notes = [pretty_midi.note_number_to_name(42)]  # C5
hihat_times = [beat * i for i in range(8)]

# Add drum hits
for note, time in zip(kick_notes, kick_times):
    drum_inst.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

for note, time in zip(snare_notes, snare_times):
    drum_inst.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

for note, time in zip(hihat_notes, hihat_times):
    drum_inst.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05))

pm.instruments.append(drum_inst)

# ---------------------------
# Bar 2-4 - Full ensemble
# Dm key, 160 BPM, 4/4 time

# Tenor Sax (You) - melody with space, searching, yearning
sax_program = pretty_midi.instrument_program('萨克斯')  # 'Saxophone' in Chinese
sax_inst = pretty_midi.Instrument(program=sax_program)

# Dm scale: D, Eb, F, G, Ab, Bb, C
# Tenor sax range: usually Bb (concert C), but we'll use concert pitches
# Let's use D (concert D), F (concert F), Ab (concert Ab), etc.

# Melody (in Dm, 4 bars) - searching, yearning, with space
# Bar 2 (0-1.5s)
# Start with a motif, leave it hanging, come back
melody_notes = [
    ('D4', 0.0),  # D4 (concert D)
    ('F4', 0.5),  # F4
    ('Ab4', 1.0),  # Ab4
    ('F4', 1.25),  # F4 again, lingering
    ('D4', 1.5),  # D4 again, setup for return

    ('D4', 1.5),  # Repeat the motif at Bar 3
    ('F4', 2.0),
    ('Ab4', 2.5),
    ('F4', 2.75),
    ('D4', 3.0),

    ('D4', 3.0),  # Bar 4, final return
    ('F4', 3.5),
    ('Ab4', 4.0),
    ('F4', 4.25),
    ('D4', 4.5),
]

# Convert note names to MIDI pitches
for note_name, start_time in melody_notes:
    pitch = pretty_midi.note_name_to_number(note_name)
    sax_inst.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + 0.25))

pm.instruments.append(sax_inst)

# ---------------------------
# Bass (Marcus) - walking line, chromatic approaches, no repeated notes
bass_program = pretty_midi.instrument_program('大提琴')  # 'Double Bass' in Chinese
bass_inst = pretty_midi.Instrument(program=bass_program)

# Dm bass line: D, Eb, F, G, Ab, Bb, C, D
# Walking line on Dm, chromatic approaches
# Bar 2-4: 3 bars, 4 beats each

# Dm walking bass line (root, b9, 11, 13, etc.)
bass_notes = [
    ('D2', 0.0),  # D2
    ('Eb2', 0.25),  # Eb2
    ('F2', 0.5),  # F2
    ('G2', 0.75),  # G2

    ('Ab2', 1.0),  # Ab2
    ('Bb2', 1.25),  # Bb2
    ('C2', 1.5),  # C2
    ('D2', 1.75),  # D2

    ('D2', 2.0),
    ('Eb2', 2.25),
    ('F2', 2.5),
    ('G2', 2.75),

    ('Ab2', 3.0),
    ('Bb2', 3.25),
    ('C2', 3.5),
    ('D2', 3.75),

    ('D2', 4.0),
    ('Eb2', 4.25),
    ('F2', 4.5),
    ('G2', 4.75),
]

for note_name, start_time in bass_notes:
    pitch = pretty_midi.note_name_to_number(note_name)
    bass_inst.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=start_time + 0.25))

pm.instruments.append(bass_inst)

# ---------------------------
# Piano (Diane) - 7th chords, comp on 2 and 4
piano_program = pretty_midi.instrument_program('钢琴')
piano_inst = pretty_midi.Instrument(program=piano_program)

# Dm7 = D, F, Ab, C
# Comp on 2 and 4

# Bar 2 (0-1.5s): comp on beat 2 (0.5s) and beat 4 (1.25s)
# Bar 3 (1.5-3s): comp on beat 2 (2.0s) and beat 4 (2.75s)
# Bar 4 (3-4.5s): comp on beat 2 (3.5s) and beat 4 (4.25s)

piano_notes = [
    ('F3', 0.5),  # Dm7 - F
    ('Ab3', 0.5),  # Ab
    ('C3', 0.5),  # C

    ('F3', 1.25),
    ('Ab3', 1.25),
    ('C3', 1.25),

    ('F3', 2.0),
    ('Ab3', 2.0),
    ('C3', 2.0),

    ('F3', 2.75),
    ('Ab3', 2.75),
    ('C3', 2.75),

    ('F3', 3.5),
    ('Ab3', 3.5),
    ('C3', 3.5),

    ('F3', 4.25),
    ('Ab3', 4.25),
    ('C3', 4.25),
]

for note_name, start_time in piano_notes:
    pitch = pretty_midi.note_name_to_number(note_name)
    piano_inst.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start_time, end=start_time + 0.25))

pm.instruments.append(piano_inst)

# ---------------------------
# Save to MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
