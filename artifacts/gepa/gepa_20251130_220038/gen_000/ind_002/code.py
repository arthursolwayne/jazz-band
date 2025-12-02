
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1 & 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 & 4
    (42, 1.125, 0.1875), # Hihat on 4
    (38, 1.5, 0.375)     # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    (20, 1.5, 0.375),    # Fm root
    (21, 1.875, 0.375),  # Fm b9
    (22, 2.25, 0.375),   # Fm 9
    (20, 2.625, 0.375),  # Fm root
    (19, 2.999, 0.375),  # Fm b7
    (18, 3.375, 0.375),  # Fm b6
    (17, 3.75, 0.375),   # Fm b5
    (19, 4.125, 0.375),  # Fm b7
    (20, 4.5, 0.375),    # Fm root
    (21, 4.875, 0.375),  # Fm b9
    (22, 5.25, 0.375),   # Fm 9
    (20, 5.625, 0.375)   # Fm root
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    (39, 1.5, 0.375),    # F7 (39=F, 41=Bb, 43=C, 46=E)
    (41, 1.5, 0.375),
    (43, 1.5, 0.375),
    (46, 1.5, 0.375),
    (41, 1.875, 0.375),  # Bb7 (41=Bb, 43=C, 46=E, 48=G)
    (43, 1.875, 0.375),
    (46, 1.875, 0.375),
    (48, 1.875, 0.375),
    (39, 2.25, 0.375),   # F7
    (41, 2.25, 0.375),
    (43, 2.25, 0.375),
    (46, 2.25, 0.375),
    (41, 2.625, 0.375),  # Bb7
    (43, 2.625, 0.375),
    (46, 2.625, 0.375),
    (48, 2.625, 0.375),
    (39, 3.0, 0.375),    # F7
    (41, 3.0, 0.375),
    (43, 3.0, 0.375),
    (46, 3.0, 0.375),
    (41, 3.375, 0.375),  # Bb7
    (43, 3.375, 0.375),
    (46, 3.375, 0.375),
    (48, 3.375, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5)
    # Add notes to drums
    drums.notes.append(kick1)
    drums.notes.append(kick3)
    drums.notes.append(snare2)
    drums.notes.append(snare4)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)

# Dante on sax (short motif, make it sing, start it, leave it hanging, come back and finish it)
sax_notes = [
    (62, 1.5, 0.5),      # F (start of motif)
    (64, 2.0, 0.375),    # A (first resolution)
    (61, 2.375, 0.375),  # E (second resolution)
    (62, 2.75, 0.375),   # F (repeat motif)
    (64, 3.125, 0.375),   # A (repeat resolution)
    (61, 3.5, 0.375),     # E (repeat resolution)
    (62, 3.875, 0.375),  # F (final repeat)
    (64, 4.25, 0.375),   # A (final resolution)
    (61, 4.625, 0.375)   # E (final resolution)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
