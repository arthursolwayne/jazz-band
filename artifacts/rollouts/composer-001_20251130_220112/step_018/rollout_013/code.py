
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

# Bar 2: Everyone in. Sax takes the melody
# Dm7 chord: D F A C
# Start with a short motif: D F A (Dm triad), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line in Dm
# Dm scale: D, Eb, F, G, A, Bb, C
# Chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=2.125, end=2.25), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.375), # C
    pretty_midi.Note(velocity=80, pitch=69, start=2.375, end=2.5),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Dm7 = D F A C
# Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875), # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375), # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375), # C
]
piano.notes.extend(piano_notes)

# Bar 3: Sax repeats motif, slightly altered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Marcus: Walking again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=2.875, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=80, pitch=70, start=3.125, end=3.25), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.375), # C
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875), # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=2.875), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=2.875), # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=2.875), # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.375), # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375), # A
]
piano.notes.extend(piano_notes)

# Bar 4: Sax resolves motif with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.625, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.125),  # A
]
sax.notes.extend(sax_notes)

# Marcus: Walking again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.875, end=4.0),   # D
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.125),  # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875), # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=3.875), # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875), # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25), # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.25), # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.25), # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.25), # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
