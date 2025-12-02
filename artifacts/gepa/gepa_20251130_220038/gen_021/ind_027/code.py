
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [i * 0.375 for i in range(0, 16)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    (1.5, 48),  # D
    (1.75, 49),  # Eb
    (2.0, 50),  # E
    (2.25, 51),  # F
    # Bar 3
    (2.5, 52),  # F#
    (2.75, 53),  # G
    (3.0, 51),  # F
    (3.25, 50),  # E
    # Bar 4
    (3.5, 49),  # Eb
    (3.75, 48),  # D
    (4.0, 47),  # C
    (4.25, 46),  # Bb
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 60),  # C
    (2.0, 64),  # E
    (2.0, 67),  # G
    (2.0, 71),  # B
    # Bar 3
    (3.0, 60),  # C
    (3.0, 64),  # E
    (3.0, 67),  # G
    (3.0, 71),  # B
    # Bar 4
    (4.0, 60),  # C
    (4.0, 64),  # E
    (4.0, 67),  # G
    (4.0, 71),  # B
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62),  # D
    (1.75, 64),  # E
    (2.0, 65),  # F
    (2.25, 62),  # D
    (2.5, 67),  # G
    (2.75, 65),  # F
    (3.0, 64),  # E
    (3.25, 62),  # D
    (3.5, 67),  # G
    (3.75, 64),  # E
    (4.0, 62),  # D
    (4.25, 65),  # F
    (4.5, 67),  # G
    (4.75, 64),  # E
    (5.0, 62),  # D
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
