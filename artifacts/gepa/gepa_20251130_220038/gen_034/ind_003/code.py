
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bass line (Marcus): Walking line, chromatic approaches, no same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.75),  # Fm7: F, Ab, Bb, D
    pretty_midi.Note(velocity=90, pitch=45, start=1.75, end=2.0),  # Gb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # E (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # D (Fm7)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=41, start=2.5, end=2.75),  # C (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=44, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=43, start=3.25, end=3.5),  # E
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=44, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=4.25, end=4.5),  # Gb
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=42, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=95, pitch=45, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=47, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=50, start=1.75, end=2.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=44, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=95, pitch=47, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=50, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=52, start=2.75, end=3.0),  # Db
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=42, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=95, pitch=45, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=95, pitch=47, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=95, pitch=50, start=4.25, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=52, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=1.875),  # F
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=52, start=2.875, end=3.0),  # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=3.875, end=4.0),  # A
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
