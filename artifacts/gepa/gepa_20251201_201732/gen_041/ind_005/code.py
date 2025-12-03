
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, C, etc.)
bass_notes = [
    # Bar 2: F -> Ab -> D -> C
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # C2
    # Bar 3: Bb -> F -> Ab -> Eb
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # Eb2
    # Bar 4: G -> Bb -> F -> Ab
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # Ab2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, one chord per bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Eb5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Ab5
    # Bar 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Eb5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # Ab4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),   # Ab4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),   # Ab4
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),   # Ab4
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),   # Ab4
]
sax.notes.extend(sax_notes)

# Drums: Continue the same pattern for bars 2-4
for i in range(2):
    for note in drum_notes:
        note_start = note.start + 1.5 + i * 1.5
        note.end = note.end + 1.5 + i * 1.5
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note_start,
            end=note.end
        )
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
