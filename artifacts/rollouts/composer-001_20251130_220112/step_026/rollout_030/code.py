
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
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125), # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.125, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375), # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.375, end=2.5), # A
]
bass.notes.extend(bass_notes)

# Diane: Piano comping on 2 and 4 with 7th chords
# Bar 2: Dm7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0), # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0), # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0), # C
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5), # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5), # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5), # C
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0), # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0), # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0), # A
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0), # C
]
piano.notes.extend(piano_notes)

# Dante: Sax melody in Dm, one short motif, start it, leave it hanging
# Motif: D - F - A - Eb (Dm triad with chromatic approach)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0), # A
    # Bar 3: Let it hang, then come back
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5), # A
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0), # A
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
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

# Bar 4: Drums continue (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
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

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
