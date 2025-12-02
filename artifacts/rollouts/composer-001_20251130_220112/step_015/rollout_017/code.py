
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
    (36, 0.0, 0.375), # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1& 
    (42, 0.1875, 0.1875), # Hihat on 2& 
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2& 
    (42, 0.5625, 0.1875), # Hihat on 3& 
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3& 
    (42, 0.9375, 0.1875), # Hihat on 4& 
    (38, 1.125, 0.375), # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (F - G - Ab - A - Bb - B - C - Db - D - Eb - F)
bass_notes = [
    (53, 1.5, 0.375), # F
    (55, 1.875, 0.375), # G
    (56, 2.25, 0.375), # Ab
    (57, 2.625, 0.375), # A
    (58, 3.0, 0.375), # Bb
    (59, 3.375, 0.375), # B
    (60, 3.75, 0.375), # C
    (61, 4.125, 0.375), # Db
    (62, 4.5, 0.375), # D
    (63, 4.875, 0.375), # Eb
    (53, 5.25, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords comping on 2 and 4
# F7 (F A C Eb) on beat 2 (1.875s)
# Bb7 (Bb D F Ab) on beat 4 (3.375s)
# F7 on beat 2 (4.125s)
# Bb7 on beat 4 (5.625s)
piano_notes = [
    # F7 on beat 2 (1.875)
    (53, 1.875, 0.375), 
    (60, 1.875, 0.375),
    (65, 1.875, 0.375),
    (63, 1.875, 0.375),
    # Bb7 on beat 4 (3.375)
    (58, 3.375, 0.375),
    (63, 3.375, 0.375),
    (65, 3.375, 0.375),
    (67, 3.375, 0.375),
    # F7 on beat 2 (4.125)
    (53, 4.125, 0.375),
    (60, 4.125, 0.375),
    (65, 4.125, 0.375),
    (63, 4.125, 0.375),
    # Bb7 on beat 4 (5.625)
    (58, 5.625, 0.375),
    (63, 5.625, 0.375),
    (65, 5.625, 0.375),
    (67, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax melody (start on bar 2)
# Motif: F - Bb - Ab - F (sings, hangs, returns in bar 4)
sax_notes = [
    (53, 1.875, 0.375), # F
    (58, 2.25, 0.375), # Bb
    (56, 2.625, 0.375), # Ab
    (53, 3.0, 0.375), # F
    (53, 4.125, 0.375), # F (return)
    (58, 4.5, 0.375), # Bb
    (56, 4.875, 0.375), # Ab
    (53, 5.25, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Full bar 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
