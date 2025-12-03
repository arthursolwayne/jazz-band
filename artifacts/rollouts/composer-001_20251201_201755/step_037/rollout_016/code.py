
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    # D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=43, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=38, start=2.8125, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: Motif in D, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: D (62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Leave it hanging on E (64) on beat 2
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),
    # Come back and finish it on F# (67) on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    # End with D (62) on beat 4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 3 (3.0 - 4.5s)
    # G2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=38, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=39, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=43, start=4.3125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation
sax_notes = [
    # Bar 3: Motif continuation
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 4 (4.5 - 6.0s)
    # B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=43, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=47, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=46, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=43, start=5.8125, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: C#7 (C#, E#, G#, B)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=6.0),  # C#4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),  # E#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # G#4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    # Bar 4: Motif resolution
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
