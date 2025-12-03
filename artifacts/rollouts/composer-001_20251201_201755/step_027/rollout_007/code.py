
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2 (fifth of Dm)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),   # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=3.0),  # D4 (root)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # F4 (third)
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=3.0),  # A4 (fifth)
    pretty_midi.Note(velocity=90, pitch=80, start=1.5, end=3.0),  # C5 (seventh)
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s)
# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # A2 (fifth of Dm)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),   # D2
]
bass.notes.extend(bass_notes)

# Diane: Cm7 (E, G, C, E) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # C4 (root)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # E4 (third)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # G4 (fifth)
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=4.5),  # Bb4 (seventh)
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s)
# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # A2 (fifth of Dm)
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),   # F2
]
bass.notes.extend(bass_notes)

# Diane: G7 (B, D, G, B) - open voicing, resolve on last bar
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=6.0),  # G4 (root)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),  # B4 (third)
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=6.0),  # D5 (fifth)
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=6.0),  # F#5 (seventh)
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # E4 (third of Dm)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),   # F#4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # G4 (fifth)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # F#4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # E4 (third)
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # D4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # E4 (third)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # F#4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # G4 (fifth)
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # F#4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # E4 (third)
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # D4 (root)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
