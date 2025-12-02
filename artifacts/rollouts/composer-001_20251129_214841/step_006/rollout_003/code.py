
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3 (beat 0 and 2)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4 (beat 1 and 3)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time signature is 4/4, 120 BPM (each beat is 0.5s)

# Bass line: Marcus (walking line, chromatic approaches, no same note twice)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.5),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.0 + 0.5),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.5 + 0.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.0 + 0.5),  # D#
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.5 + 0.5),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.0 + 0.5),  # F#
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.5 + 0.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.0 + 0.5),  # G#
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.125),  # Bb
    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.5 + 0.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.5 + 0.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.5 + 0.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.5 + 0.125),  # Bb
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.0 + 0.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.0 + 0.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.0 + 0.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.0 + 0.125),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3 (beat 0 and 2)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.5)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.0, end=start + 1.5)
    # Snare on 2 and 4 (beat 1 and 3)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.5, end=start + 1.0)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.5, end=start + i * 0.5 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: Dante (melody in bars 2-4)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C (60), E (64), D (62), Bb (71) — a simple, angular, bluesy motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.75 + 0.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.0 + 0.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.25 + 0.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.5 + 0.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.75 + 0.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.0 + 0.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.25 + 0.25),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
