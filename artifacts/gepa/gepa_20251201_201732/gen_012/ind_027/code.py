
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
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, root and fifth with chromatic approaches
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    # D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    # Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    # Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    # Dm7 (resolving)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif - short, singable, starts and ends with a question
sax_notes = [
    # Dm (D, F, A)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    # Leave it hanging, come back
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Repeat bass, piano, and sax with variations
# Bass repeats the same walking line
bass_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes_2)

# Piano: Same chords again
piano_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes_2)

# Sax: Repeat motif but with a slight variation
sax_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.375),
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5),
]
sax.notes.extend(sax_notes_2)

# Bar 3: Drums continue
drum_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes_2)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
