
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (0.0 + 1.5, 50, 100),  # D2 (root)
    (0.375 + 1.5, 53, 90),  # Eb2 (chromatic approach)
    (0.75 + 1.5, 57, 100),  # A2 (fifth)
    (1.125 + 1.5, 50, 100), # D2 (root)
    # Bar 3
    (1.5 + 1.5, 50, 100),   # D2
    (1.875 + 1.5, 53, 90),  # Eb2
    (2.25 + 1.5, 57, 100),  # A2
    (2.625 + 1.5, 50, 100), # D2
    # Bar 4
    (3.0 + 1.5, 50, 100),   # D2
    (3.375 + 1.5, 53, 90),  # Eb2
    (3.75 + 1.5, 57, 100),  # A2
    (4.125 + 1.5, 50, 100), # D2
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = [
    (0.0 + 1.5, 62, 100),  # D4
    (0.0 + 1.5, 67, 100),  # F#4
    (0.0 + 1.5, 69, 100),  # A4
    (0.0 + 1.5, 72, 100),  # C#5
]
# Bar 3: G7 (G B D F)
for note in piano_notes:
    note.pitch += 4
    note.start += 1.5
    piano.notes.append(note)
# Bar 4: C7 (C E G B)
for note in piano_notes:
    note.pitch -= 2
    note.start += 3.0
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 - B4 (over 2 bars)
sax_notes = [
    (0.0 + 1.5, 62, 100),  # D4
    (0.375 + 1.5, 67, 100), # F#4
    (0.75 + 1.5, 69, 100),  # A4
    (1.125 + 1.5, 71, 100), # B4
    # Repeat the motif slightly altered in the next bar
    (1.5 + 1.5, 62, 100),   # D4
    (1.875 + 1.5, 67, 100), # F#4
    (2.25 + 1.5, 69, 100),  # A4
    (2.625 + 1.5, 71, 100), # B4
    # End with a resolution on D5
    (3.0 + 1.5, 72, 100),   # D5
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
