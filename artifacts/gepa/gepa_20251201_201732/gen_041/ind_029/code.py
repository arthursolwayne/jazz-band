
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (Bar 2, beat 1)
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),
    # G2 (Bar 2, beat 2)
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),
    # A#2 (chromatic approach to Bb2) - Bar 2, beat 3
    pretty_midi.Note(velocity=90, pitch=80, start=2.25, end=2.625),
    # Bb2 (Bar 2, beat 4)
    pretty_midi.Note(velocity=90, pitch=81, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif - Start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Motif (Bb4, D5, Bb4)
    pretty_midi.Note(velocity=110, pitch=81, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=84, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=81, start=2.25, end=2.625),
    # Bar 3: Motif repeat (Bb4, D5, Bb4)
    pretty_midi.Note(velocity=110, pitch=81, start=2.625, end=2.9375),
    pretty_midi.Note(velocity=110, pitch=84, start=2.9375, end=3.25),
    pretty_midi.Note(velocity=110, pitch=81, start=3.25, end=3.625),
    # Bar 4: Motif variation (Bb4, D5, F5)
    pretty_midi.Note(velocity=110, pitch=81, start=3.625, end=3.9375),
    pretty_midi.Note(velocity=110, pitch=84, start=3.9375, end=4.25),
    pretty_midi.Note(velocity=110, pitch=87, start=4.25, end=4.625),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in F (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bb2 (Bar 3, beat 1)
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),
    # C3 (Bar 3, beat 2)
    pretty_midi.Note(velocity=90, pitch=83, start=3.375, end=3.75),
    # D#2 (chromatic approach to Eb2) - Bar 3, beat 3
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.125),
    # Eb2 (Bar 3, beat 4)
    pretty_midi.Note(velocity=90, pitch=83, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Motif - Start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 3: Motif (Bb4, D5, Bb4)
    pretty_midi.Note(velocity=110, pitch=81, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=84, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=81, start=3.75, end=4.125),
    # Bar 4: Motif repeat (Bb4, D5, Bb4)
    pretty_midi.Note(velocity=110, pitch=81, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=84, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=81, start=4.875, end=5.25),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in F (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Eb2 (Bar 4, beat 1)
    pretty_midi.Note(velocity=90, pitch=83, start=4.5, end=4.875),
    # F2 (Bar 4, beat 2)
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),
    # G2 (Bar 4, beat 3)
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),
    # A#2 (chromatic approach to Bb2) - Bar 4, beat 4
    pretty_midi.Note(velocity=90, pitch=80, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif - Start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 4: Motif (Bb4, D5, Bb4)
    pretty_midi.Note(velocity=110, pitch=81, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=84, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=81, start=5.25, end=5.625),
    # Final note to leave it hanging
    pretty_midi.Note(velocity=110, pitch=84, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
for bar in range(2, 4):
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.1875, end=start_time + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
