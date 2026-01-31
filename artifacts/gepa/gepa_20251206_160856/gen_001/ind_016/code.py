
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
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

# Bass: Walking line in Dm - D2, G2, C2, F2 with chromatic approaches
bass_notes = [
    # D2 (root) with chromatic approach from C#
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # G2 (fifth) with chromatic approach from F#
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),
    # C2 (bass note) with chromatic approach from B
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),
    # F2 (bass note) with chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0)   # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Dm scale - D, Eb, F, G
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D5
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)   # G5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm - D2, G2, C2, F2 with chromatic approaches
bass_notes = [
    # D2 (root) with chromatic approach from C#
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),
    # G2 (fifth) with chromatic approach from F#
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),
    # C2 (bass note) with chromatic approach from B
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),
    # F2 (bass note) with chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: C7 (C E G B) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5)   # B5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Repeat the motif with a slight variation
sax_notes = [
    # Dm scale - D, Eb, F, G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # Eb5
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5)   # G5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm - D2, G2, C2, F2 with chromatic approaches
bass_notes = [
    # D2 (root) with chromatic approach from C#
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    # G2 (fifth) with chromatic approach from F#
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),
    # C2 (bass note) with chromatic approach from B
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),
    # F2 (bass note) with chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Gm7 (G Bb D F) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # Bb5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # D6
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0)   # F6
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Repeat the motif with a slight variation
sax_notes = [
    # Dm scale - D, Eb, F, G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # Eb5
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)   # G5
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
