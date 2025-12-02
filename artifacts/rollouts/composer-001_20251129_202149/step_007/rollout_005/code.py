
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.6875, end=1.875), # C#
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.0625, end=2.25), # D#
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.4375), # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.4375, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=66, start=2.625, end=2.8125), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.8125, end=3.0), # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),
    # Bar 2, beat 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125),
    # Bar 3, beat 2: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625),
    # Bar 3, beat 4: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.3125),
    # Bar 4, beat 2: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0625),
    # Bar 4, beat 4: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125),
]
piano.notes.extend(piano_notes)

# Drums: continue with same pattern
for i in range(3):
    for note in drum_notes:
        note.start += 1.5 + i * 1.5
        note.end += 1.5 + i * 1.5
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875), # E
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=110, pitch=63, start=2.125, end=2.25), # D
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75), # E
    pretty_midi.Note(velocity=110, pitch=68, start=2.75, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Add the instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
