
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0), # A2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # A2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75), # C3
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125), # C#3
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5), # E3
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875), # E3
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # G3
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # G#3
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0), # B3
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fmaj7
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0), # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0), # C5
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0), # E5
    # Bar 3 (3.0 - 4.5s) - Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=4.5), # G4
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=4.5), # Bb4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5), # D5
    # Bar 4 (4.5 - 6.0s) - G7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0), # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0), # D5
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=6.0), # F#5
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75), # F5
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0), # A5
    pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.25), # G5
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5), # F5
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.25), # A5
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5), # G5
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75), # F5
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.0), # A5
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.75), # G5
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0), # F5
    pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.25), # A5
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.5), # G5
    pretty_midi.Note(velocity=110, pitch=72, start=5.5, end=5.75), # F5
    pretty_midi.Note(velocity=110, pitch=76, start=5.75, end=6.0), # A5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
