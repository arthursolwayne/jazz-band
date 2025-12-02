
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.625, end=1.75), # E
    pretty_midi.Note(velocity=100, pitch=43, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.0), # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=45, start=2.0, end=2.125), # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=2.125, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=100, pitch=41, start=2.375, end=2.5), # E
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=2.75), # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=2.75, end=2.875), # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=2.875, end=3.0), # B
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.0), # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.0), # D
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.0), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0), # G
    # Bar 3, beat 2
    pretty_midi.Note(velocity=100, pitch=46, start=2.625, end=2.75), # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=2.75), # D
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=2.75), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=2.75), # G
    # Bar 4, beat 2
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.5), # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.5), # D
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.5), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.5), # G
]
piano.notes.extend(piano_notes)

# Drums in bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.375), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.625), # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=2.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=3.75), # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.5), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.625, end=4.75), # Snare on 4
]
# Hihat on every eighth in bars 2-4
for t in range(1.5, 6.0, 0.125):
    if t % 1.0 != 0:
        pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.125)
drums.notes.extend(drum_notes)

# Sax (Dante): Start with a short motif, leave it hanging, come back
# Fm7: F, Ab, Bb, D
note_lengths = [0.375, 0.375, 0.25, 0.25]
note_pitches = [53, 50, 46, 49]  # F, Ab, Bb, D
start = 1.5
for i, (pitch, length) in enumerate(zip(note_pitches, note_lengths)):
    pretty_midi.Note(velocity=110, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + length)
# Leave it hanging
pretty_midi.Note(velocity=110, pitch=50, start=2.625, end=2.75)  # Ab
# Come back and finish it
pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.5)  # F
pretty_midi.Note(velocity=110, pitch=49, start=3.5, end=3.625)  # D

sax.notes.extend([note for note in sax.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_moment.mid")
