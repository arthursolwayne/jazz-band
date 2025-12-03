
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Bass: walking line with chromatic approach on D
bass_notes = [
    # D2 (D3 in MIDI, 50)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),
    # Chromatic approach to Eb2 (MIDI 51)
    pretty_midi.Note(velocity=60, pitch=51, start=1.875, end=2.0),
    # G2 (MIDI 55)
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.375),
    # F2 (MIDI 53)
    pretty_midi.Note(velocity=90, pitch=53, start=2.375, end=2.75),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),
    # Bar 3: Bm7b5 (B, D, F#, A)
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.5),
    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=90, pitch=78, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: haunting motif, start it, leave it hanging
sax_notes = [
    # Bar 2: Start with a short motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Similar to bar 1, but with a slight variation
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 3: Bass (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=60, pitch=51, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=55, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=53, start=3.875, end=4.25),
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (3.0 - 4.5s)
piano_notes = [
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Sax (3.0 - 4.5s)
sax_notes = [
    # Bar 3: Extend the motif with a higher note
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # B4
]
sax.notes.extend(sax_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Similar to bar 1, but with a slightly more aggressive snare
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.125, end=6.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Bass (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=60, pitch=51, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.375),
    pretty_midi.Note(velocity=90, pitch=53, start=5.375, end=5.75),
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (4.5 - 6.0s)
piano_notes = [
    # Bar 4: D7 with a tritone substitution (G7)
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),
]
piano.notes.extend(piano_notes)

# Bar 4: Sax (4.5 - 6.0s)
sax_notes = [
    # Bar 4: Resolve the motif
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
