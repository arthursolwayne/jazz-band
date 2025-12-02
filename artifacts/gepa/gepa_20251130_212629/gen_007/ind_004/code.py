
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray on drums alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in [0]:  # only bar 1
    for beat in range(4):  # 4 beats per bar
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.125))
        for eighth in range(2):
            drum_notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.03125))

# Add the drum notes
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus on walking line with chromatic approaches
bass_notes = []
for bar in range(1, 4):  # bars 2, 3, 4
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        # Walk in D minor with chromatic passing tones
        if beat == 0:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=time, end=time + 0.25))  # D (62)
        elif beat == 1:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=time, end=time + 0.25))  # Eb (63)
        elif beat == 2:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=61, start=time, end=time + 0.25))  # C (61)
        elif beat == 3:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=time, end=time + 0.25))  # F (64)

bass.notes.extend(bass_notes)

# Piano: Diane – 7th chords, comp on 2 and 4
piano_notes = []
for bar in range(1, 4):  # bars 2, 3, 4
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        # D7 on beat 2 and 4
        if beat == 1 or beat == 3:
            # D7: D (62), F# (67), A (69), C (60)
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.25))
            piano_notes.append(pretty_midi.Note(velocity=85, pitch=67, start=time, end=time + 0.25))
            piano_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=time, end=time + 0.25))
            piano_notes.append(pretty_midi.Note(velocity=75, pitch=60, start=time, end=time + 0.25))

piano.notes.extend(piano_notes)

# Sax: Dante – melody in D minor, haunting and sparse
sax_notes = []

# Bar 2: Start the motif
bar2_start = 1.5
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + 0.25))  # D
sax_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 0.5, end=bar2_start + 0.75))  # Bb
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 0.75, end=bar2_start + 1.0))  # D

# Bar 3: No sax (leave space)
# Bar 4: Come back and finish the motif
bar4_start = 4.5
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar4_start, end=bar4_start + 0.25))  # F
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar4_start + 0.5, end=bar4_start + 0.75))  # D
sax_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar4_start + 0.75, end=bar4_start + 1.0))  # Bb

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
