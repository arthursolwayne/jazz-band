
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line (F2 to G2), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=54, start=1.875, end=2.25),
    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),
    # F2 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, each bar different chord, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0)   # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2 to G2), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),
    # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75),
    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),
    # F2 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75)
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=4.25, end=4.5)   # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2 to G2), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),
    # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.25),
    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),
    # F2 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C E G B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25)
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=5.75, end=6.0)   # D
]
sax.notes.extend(sax_notes)

# Drums: Continue the pattern for bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0)
]
# Hi-hats on every eighth
for i in range(3):
    start = 3.0 + i * 1.5
    for j in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)
drums.notes.extend(drum_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
