
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass (D2-G2, MIDI 38-43), walking line with chromatic approaches
bass_notes = [
    # D2 (38) on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # F (41) on beat 2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # G2 (43) on beat 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    # D2 (38) on beat 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane on piano, open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F5
]
piano.notes.extend(piano_notes)

# Bar 4: Am7 (A-C-E-G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # G5
]
piano.notes.extend(piano_notes)

# Dante on sax: short motif, melodic, one phrase, leave it hanging
# Start on D (62), then F (65), then C (67), then resolve with a D (62) on the last beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Little Ray continues
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 6.0s)
# Marcus continues walking line
bass_notes = [
    # D2 (38) on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # F (41) on beat 2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),
    # G2 (43) on beat 3
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),
    # D2 (38) on beat 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Diane continues comping on 2 and 4
# Bar 3: comp on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # F5
]
piano.notes.extend(piano_notes)

# Bar 4: comp on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # G5
]
piano.notes.extend(piano_notes)

# Dante on sax: continue the motif, resolve the phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
