
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (43)
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),
    
    # Bar 3: G2 (43)
    pretty_midi.Note(velocity=80, pitch=43, start=2.375, end=2.75),
    # Chromatic approach to B2 (46)
    pretty_midi.Note(velocity=70, pitch=45, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=46, start=2.875, end=3.25),
    
    # Bar 4: B2 (46)
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.625),
    # Chromatic approach to D3 (50)
    pretty_midi.Note(velocity=70, pitch=49, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=2.0),  # C#5
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.375, end=2.875),  # G4
    pretty_midi.Note(velocity=80, pitch=72, start=2.375, end=2.875),  # B4
    pretty_midi.Note(velocity=80, pitch=76, start=2.375, end=2.875),  # D5
    pretty_midi.Note(velocity=80, pitch=81, start=2.375, end=2.875),  # F5
])
# Bar 4: Bm7 (B-D-F#-A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.75),  # B4
    pretty_midi.Note(velocity=80, pitch=76, start=3.25, end=3.75),  # D5
    pretty_midi.Note(velocity=80, pitch=81, start=3.25, end=3.75),  # F#5
    pretty_midi.Note(velocity=80, pitch=86, start=3.25, end=3.75),  # A5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - D4 - B3 (MIDI 62-67-62-60)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.125),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.5),  # D4
    pretty_midi.Note(velocity=120, pitch=60, start=2.5, end=2.875),  # B3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.625),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=4.0),  # D4
    pretty_midi.Note(velocity=120, pitch=60, start=4.0, end=4.375),  # B3
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
