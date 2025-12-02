
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick_1)
drums.notes.append(drum_kick_2)

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)
drums.notes.append(drum_snare_1)
drums.notes.append(drum_snare_2)

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # A#
    pretty_midi.Note(velocity=80, pitch=72, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=73, start=4.25, end=4.5),  # C#
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=5.0),  # D#
    pretty_midi.Note(velocity=80, pitch=77, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=80, pitch=80, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=81, start=5.75, end=6.0),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # D
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.25),  # D
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.75),  # D
    # Bar 2 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.25),  # D
    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.75),  # D
    # Bar 4 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    # Bar 2 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.75),  # D
    # Bar 3 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    # Bar 4 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # D
    # Bar 2 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    # Bar 3 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # D
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25),  # D
    # Bar 2 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # D
    # Bar 3 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25),  # D
    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # D
    # Bar 2 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25),  # D
    # Bar 3 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # D
    # Bar 4 (5.0 - 5.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.25),  # D
    # Bar 2 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # D
    # Bar 3 (5.0 - 5.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.25),  # D
    # Bar 4 (5.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.5, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs

# Bar 2 (1.5 - 2.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # Bb
]

# Bar 3 (2.0 - 2.5s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25))  # G

# Bar 4 (2.5 - 3.0s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75))  # Bb
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0))  # B

# Bar 2 (3.0 - 3.5s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25))  # G

# Bar 3 (3.5 - 4.0s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75))  # Bb
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0))  # B

# Bar 2 (4.0 - 4.5s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25))  # G

# Bar 3 (4.5 - 5.0s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75))  # Bb
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0))  # B

# Bar 2 (5.0 - 5.5s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25))  # G

# Bar 3 (5.5 - 6.0s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75))  # Bb
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0))  # B

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
