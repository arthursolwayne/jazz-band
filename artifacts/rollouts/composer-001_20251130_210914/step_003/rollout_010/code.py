
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=50, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=47, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=46, start=4.25, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=49, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=47, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4, in Fm
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=2.0),  # D
    # Bar 3: Fm7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.5),  # D
    # Bar 4: Fm7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=5.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, come back and finish it
# Motif: F (64), Ab (67), C (69), Bb (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
]
sax.notes.extend(sax_notes)

# Drums: Same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
