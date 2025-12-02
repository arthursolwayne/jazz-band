
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F - G - Ab - A (walking line with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0), # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last chord (Bar 2: Fm7, Bar 3: Bbm7, Bar 4: Eb7)
piano_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # Ab5

    # Bar 3 (Bbm7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # F5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # G5
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # Bb5

    # Bar 4 (Eb7)
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0), # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # C5
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0), # Eb5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, Ab4, Bb4, F4 (start at 1.5s, end at 2.0s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875), # F4
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875), # Ab4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0), # Bb4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.8125), # F4 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=2.8125, end=3.0), # Bb4 (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue same pattern
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend(drum_notes)

# Bar 4: Drums continue same pattern
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend(drum_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('jazz_piece.mid')
