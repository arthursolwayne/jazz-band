
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
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Hihat on 1 & 2
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1875)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + 0.375, end=time + 0.5625)
    drums.notes.append(hihat)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 1.125)
    drums.notes.append(snare)
    # Hihat on 3 & 4
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + 0.75, end=time + 0.9375)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + 1.125, end=time + 1.3125)
    drums.notes.append(hihat)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.5, end=time + 1.875)
    drums.notes.append(snare)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, Ab, D, C, E, G, Bb, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
]
piano.notes.extend(piano_notes)

# Bar 3: Ab7 (Ab, C, Eb, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Bar 4: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, D, F (Fm triad with a chromatic approach)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=44, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=45, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=110, pitch=45, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=44, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=45, start=4.125, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
for bar in range(2, 4):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Hihat on 1 & 2
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1875)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + 0.375, end=time + 0.5625)
    drums.notes.append(hihat)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 1.125)
    drums.notes.append(snare)
    # Hihat on 3 & 4
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + 0.75, end=time + 0.9375)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + 1.125, end=time + 1.3125)
    drums.notes.append(hihat)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.5, end=time + 1.875)
    drums.notes.append(snare)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
