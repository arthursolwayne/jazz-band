
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
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Everyone in
# Bass: D2 (D2), F2, G2, A2
bass_notes = [
    (1.5, 38), (1.5, 40), (1.5, 43), (1.5, 45),
    (1.875, 38), (1.875, 40), (1.875, 43), (1.875, 45),
    (2.25, 38), (2.25, 40), (2.25, 43), (2.25, 45),
    (2.625, 38), (2.625, 40), (2.625, 43), (2.625, 45)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicings, different chord each bar
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 76),
    (2.25, 64), (2.25, 69), (2.25, 74), (2.25, 76),
    (3.0, 62), (3.0, 69), (3.0, 74), (3.0, 76),
    (3.75, 64), (3.75, 69), (3.75, 72), (3.75, 76)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, start it, leave it hanging
# Dm7 arpeggio with a twist on beat 3
sax_notes = [
    (1.5, 67), (1.5, 72), (1.5, 69), (1.5, 74),
    (2.25, 72), (2.25, 69), (2.25, 77), (2.25, 74),
    (3.0, 74), (3.0, 69), (3.0, 77), (3.0, 72),
    (3.75, 72), (3.75, 69), (3.75, 77), (3.75, 74)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Drums for bars 2-4
drum_notes = [
    (1.5, 36), (1.875, 38), (2.25, 36), (2.625, 38),
    (3.0, 36), (3.375, 38), (3.75, 36), (4.125, 38),
    (4.5, 36), (4.875, 38), (5.25, 36), (5.625, 38)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add hihat on every eighth
for i in range(18):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Add the rest of the drums for bar 2-4
for i in range(12):
    time = 1.5 + i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
