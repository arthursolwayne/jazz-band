
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on 2
    (42, 0.375, 0.1875), # Hihat on 3
    (42, 0.5625, 0.1875), # Hihat on 4
    (36, 1.125, 0.375), # Kick on 3
    (38, 1.5, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 3
    (42, 1.3125, 0.1875), # Hihat on 4
    (42, 1.5, 0.1875) # Hihat on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Marcus - walking bass line in Fm (F, Eb, D, C, Bb, A, G, F#)
# Chromatic approach to Fm7
bass_notes = [
    (38, 1.5, 0.375),  # F
    (37, 1.875, 0.375), # Eb
    (36, 2.25, 0.375), # D
    (35, 2.625, 0.375), # C
    (33, 3.0, 0.375), # Bb
    (32, 3.375, 0.375), # A
    (31, 3.75, 0.375), # G
    (30, 4.125, 0.375), # F#
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane - piano comping on 2 and 4 with 7th chords
# Fm7 (F, Ab, Bb, D) on beat 2
# Fm7 (F, Ab, Bb, D) on beat 4
piano_notes = [
    # Beat 2 (1.875s)
    (53, 1.875, 0.375), # F
    (51, 1.875, 0.375), # Ab
    (50, 1.875, 0.375), # Bb
    (56, 1.875, 0.375), # D
    # Beat 4 (3.0s)
    (53, 3.0, 0.375), # F
    (51, 3.0, 0.375), # Ab
    (50, 3.0, 0.375), # Bb
    (56, 3.0, 0.375), # D
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Dante - sax melody (start at bar 2, 1.5s)
# Motif: F (Ab), Bb (D), rest, F (Ab)
# Dynamic: soft, subtle, with space
sax_notes = [
    (53, 1.5, 0.375),  # F
    (51, 1.875, 0.375), # Ab
    (50, 2.25, 0.375), # Bb
    (56, 2.625, 0.375), # D
    (53, 3.0, 0.375),  # F
    (51, 3.375, 0.375), # Ab
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus - walking bass (F, Eb, D, C)
bass_notes = [
    (38, 3.0, 0.375),  # F
    (37, 3.375, 0.375), # Eb
    (36, 3.75, 0.375), # D
    (35, 4.125, 0.375), # C
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane - piano comping on 2 and 4 again with 7th chords
piano_notes = [
    # Beat 2 (3.375s)
    (53, 3.375, 0.375), # F
    (51, 3.375, 0.375), # Ab
    (50, 3.375, 0.375), # Bb
    (56, 3.375, 0.375), # D
    # Beat 4 (4.5s)
    (53, 4.5, 0.375), # F
    (51, 4.5, 0.375), # Ab
    (50, 4.5, 0.375), # Bb
    (56, 4.5, 0.375), # D
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Dante - sax motif variation (start at bar 3, 3.0s)
# Motif: Ab (Bb), D (F), rest, Ab (Bb)
sax_notes = [
    (51, 3.0, 0.375),  # Ab
    (50, 3.375, 0.375), # Bb
    (56, 3.75, 0.375), # D
    (53, 4.125, 0.375), # F
    (51, 4.5, 0.375),  # Ab
    (50, 4.875, 0.375), # Bb
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus - walking bass (Bb, A, G, F#)
bass_notes = [
    (33, 4.5, 0.375),  # Bb
    (32, 4.875, 0.375), # A
    (31, 5.25, 0.375), # G
    (30, 5.625, 0.375), # F#
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane - piano comping on 2 and 4 again with 7th chords
piano_notes = [
    # Beat 2 (4.875s)
    (53, 4.875, 0.375), # F
    (51, 4.875, 0.375), # Ab
    (50, 4.875, 0.375), # Bb
    (56, 4.875, 0.375), # D
    # Beat 4 (6.0s)
    (53, 6.0, 0.375), # F
    (51, 6.0, 0.375), # Ab
    (50, 6.0, 0.375), # Bb
    (56, 6.0, 0.375), # D
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Dante - sax motif variation (start at bar 4, 4.5s)
# Motif: Bb (D), F (Ab), rest, Bb (D)
# End with a question, leave it hanging
sax_notes = [
    (50, 4.5, 0.375),  # Bb
    (56, 4.875, 0.375), # D
    (53, 5.25, 0.375), # F
    (51, 5.625, 0.375), # Ab
    (50, 6.0, 0.375),  # Bb
    (56, 6.375, 0.375), # D
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Drums in bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on 2
    (42, 4.875, 0.1875), # Hihat on 3
    (42, 5.0625, 0.1875), # Hihat on 4
    (36, 5.25, 0.375), # Kick on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on 4
    (42, 5.625, 0.1875) # Hihat on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_in_fm.mid")
