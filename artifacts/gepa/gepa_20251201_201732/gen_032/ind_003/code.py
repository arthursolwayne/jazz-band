
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
# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) -> C#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25),  # C#2
    # Bar 3: A2 (fifth) -> B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),   # B2
    # Bar 4: D2 (root) -> C#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=37, start=3.375, end=3.75),  # C#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C#4
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # F4
    # Bar 4: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # C#4
]
piano.notes.extend(piano_notes)

# Drums: continue pattern for bars 2-4
for i in range(3):
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + 1.5 + i * 1.5,
            end=note.end + 1.5 + i * 1.5
        )
        drums.notes.append(new_note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: D4 (62) -> F#4 (67) -> A4 (71) -> D4 (62) (no scale runs, just a question)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),  # A4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
