
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
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches, not scales
bass_notes = [
    # Bar 2: F (38), C (43), F (38), Bb (41)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=41, start=1.5 + 2.25, end=1.5 + 2.25 + 0.375),

    # Bar 3: Bb (41), F (38), Bb (41), Eb (37)
    pretty_midi.Note(velocity=90, pitch=41, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=1.5 + 2.25, end=1.5 + 2.25 + 0.375),
    pretty_midi.Note(velocity=90, pitch=41, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=37, start=1.5 + 3.75, end=1.5 + 3.75 + 0.375),

    # Bar 4: Eb (37), Bb (41), Eb (37), Ab (39)
    pretty_midi.Note(velocity=90, pitch=37, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=41, start=1.5 + 3.75, end=1.5 + 3.75 + 0.375),
    pretty_midi.Note(velocity=90, pitch=37, start=1.5 + 4.5, end=1.5 + 4.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=39, start=1.5 + 5.25, end=1.5 + 5.25 + 0.375)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.5 + 0.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.375),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.5 + 0.375),  # E

    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),  # Ab

    # Bar 4: Ebmaj7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)   # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 4):
    time = 1.5 + bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Dante: Tenor sax motif. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (65), Bb (62), D (67), F (65) — with a slight chromatic approach on D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375),
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
