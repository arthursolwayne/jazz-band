
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1, 3; snare on 2, 4; hihat on every eighth, with subtle dynamic variation
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=60, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=60, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Add dynamic variation in hihat by splitting into smaller notes with varying velocities
for i in range(0, 12):
    start = i * 0.125
    end = start + 0.125
    velocity = 80 + (i % 2) * 20  # Alternate between 80 and 100
    drum_notes.append(pretty_midi.Note(velocity=velocity, pitch=42, start=start, end=end))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif: F - G - A - Bb (F7 chord), then D - Eb - F - G (Dm7)
# Start with the motif, leave it hanging, then come back and finish it.

# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=73, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=3.0),  # Eb
]

# Bar 3 (3.0 - 4.5s)
sax_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=4.25, end=4.5),  # Eb
])

# Bar 4 (4.5 - 6.0s)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=73, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=5.75, end=6.0),  # Eb
])

sax.notes.extend(sax_notes)

# Bass line: Walking line with chromatic approaches, no repeated notes
# In F7 (F A C E), then Dm7 (D F A C)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=56, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=2.75, end=3.0),  # A

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=57, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=56, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=80, pitch=53, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=4.25, end=4.5),  # E

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=80, pitch=53, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=5.75, end=6.0),  # A
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4, keep it moving with emotion
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),  # F7: F
    pretty_midi.Note(velocity=80, pitch=74, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=76, start=1.75, end=2.0),  # E

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # Dm7: D
    pretty_midi.Note(velocity=80, pitch=70, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),  # G

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),  # F7: F
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.5),  # E
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
