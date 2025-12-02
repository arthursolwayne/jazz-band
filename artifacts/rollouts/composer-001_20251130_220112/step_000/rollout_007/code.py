
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Fm7 -> Bb -> Eb -> Ab -> (rest)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=83, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=80, start=1.875, end=2.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=77, start=2.0625, end=2.25), # Ab
]
sax.notes.extend(sax_notes)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=1.75),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.75, end=2.0),     # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=2.0, end=2.25),     # D
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),     # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=87, start=1.75, end=2.0),     # F
    pretty_midi.Note(velocity=90, pitch=79, start=1.75, end=2.0),     # Ab
    pretty_midi.Note(velocity=90, pitch=77, start=1.75, end=2.0),     # C
    pretty_midi.Note(velocity=90, pitch=75, start=1.75, end=2.0),     # Eb
    # Bar 3: Bbm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=83, start=2.25, end=2.5),     # Bb
    pretty_midi.Note(velocity=90, pitch=75, start=2.25, end=2.5),     # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),     # F
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),     # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=83, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=80, start=3.375, end=3.5625), # Eb
    pretty_midi.Note(velocity=100, pitch=77, start=3.5625, end=3.75), # Ab
]
sax.notes.extend(sax_notes)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.25),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.25, end=3.5),     # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=3.5, end=3.75),     # D
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.0),     # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords comp on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=87, start=3.25, end=3.5),     # F
    pretty_midi.Note(velocity=90, pitch=79, start=3.25, end=3.5),     # Ab
    pretty_midi.Note(velocity=90, pitch=77, start=3.25, end=3.5),     # C
    pretty_midi.Note(velocity=90, pitch=75, start=3.25, end=3.5),     # Eb
    # Bar 4: Ebm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=80, start=3.75, end=4.0),     # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),     # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.0),     # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.0),     # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: return to original motif, but with a slight resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=83, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=80, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=77, start=5.0625, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=87, start=5.25, end=5.5),    # F (resolution)
]
sax.notes.extend(sax_notes)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.75),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=5.0),     # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=5.0, end=5.25),     # D
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.5),     # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords comp on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=87, start=4.75, end=5.0),     # F
    pretty_midi.Note(velocity=90, pitch=79, start=4.75, end=5.0),     # Ab
    pretty_midi.Note(velocity=90, pitch=77, start=4.75, end=5.0),     # C
    pretty_midi.Note(velocity=90, pitch=75, start=4.75, end=5.0),     # Eb
    # Bar 4: Fm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=87, start=5.25, end=5.5),     # F
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.5),     # Ab
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.5),     # C
    pretty_midi.Note(velocity=90, pitch=75, start=5.25, end=5.5),     # Eb
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
