
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    # Bar 2: D2 (root), E2 (chromatic up), F2 (b9), G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=41, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # A3
    pretty_midi.Note(velocity=85, pitch=59, start=1.5, end=3.0),  # F3
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=3.0)   # C3
]
piano.notes.extend(piano_notes)

# Sax: motif - start on E4 (MIDI 65), then Bb4 (MIDI 69), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    # Bar 3: G2 (fifth), A2 (root), Bb2 (chromatic down), C2 (b9)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=85, pitch=40, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 (F, A, D, F)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # A3
    pretty_midi.Note(velocity=85, pitch=59, start=3.0, end=4.5),  # F3
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=4.5)   # C3
]
piano.notes.extend(piano_notes)

# Sax: motif - resolve the hanging note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    # Bar 4: C2 (b9), D2 (root), Eb2 (chromatic up), F2 (b7)
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=40, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (F, A, D, F)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # A3
    pretty_midi.Note(velocity=85, pitch=59, start=4.5, end=6.0),  # F3
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=6.0)   # C3
]
piano.notes.extend(piano_notes)

# Sax: motif - return and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
