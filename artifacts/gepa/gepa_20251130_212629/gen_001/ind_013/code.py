
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1 & 2
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2 & 3
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (77, 1.5, 0.375),    # F
    (75, 1.875, 0.375),  # Gb
    (70, 2.25, 0.375),   # Ab
    (71, 2.625, 0.375),  # A
    (73, 3.0, 0.375),    # Bb
    (74, 3.375, 0.375),  # B
    (76, 3.75, 0.375),   # C
    (74, 4.125, 0.375)   # Db
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (53, 1.875, 0.1875), # F
    (55, 1.875, 0.1875), # A
    (57, 1.875, 0.1875), # C
    (59, 1.875, 0.1875), # D
    # Bar 2: Bb7 on beat 4
    (71, 3.0, 0.1875),   # Bb
    (73, 3.0, 0.1875),   # D
    (76, 3.0, 0.1875),   # F
    (78, 3.0, 0.1875),   # G
    # Bar 3: F7 on beat 2
    (53, 3.375, 0.1875), # F
    (55, 3.375, 0.1875), # A
    (57, 3.375, 0.1875), # C
    (59, 3.375, 0.1875), # D
    # Bar 3: Bb7 on beat 4
    (71, 4.5, 0.1875),   # Bb
    (73, 4.5, 0.1875),   # D
    (76, 4.5, 0.1875),   # F
    (78, 4.5, 0.1875),   # G
    # Bar 4: F7 on beat 2
    (53, 4.875, 0.1875), # F
    (55, 4.875, 0.1875), # A
    (57, 4.875, 0.1875), # C
    (59, 4.875, 0.1875), # D
    # Bar 4: Bb7 on beat 4
    (71, 6.0, 0.1875),   # Bb
    (73, 6.0, 0.1875),   # D
    (76, 6.0, 0.1875),   # F
    (78, 6.0, 0.1875),   # G
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.1875),  # Hihat on 1 & 2
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875),# Hihat on 2 & 3
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3 & 4
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1 & 2
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875),# Hihat on 2 & 3
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3 & 4
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1 & 2
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875),# Hihat on 2 & 3
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3 & 4
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Bar 2: Motif
# Fm motif: F, Ab, Bb, C
sax_notes = [
    (77, 1.5, 0.375),   # F
    (70, 1.875, 0.375), # Ab
    (73, 2.25, 0.375),  # Bb
    (76, 2.625, 0.375), # C
    # Leave it hanging - no note on beat 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Repeat motif but lower
# Fm motif: F, Ab, Bb, C - same but lower in register
sax_notes = [
    (77 - 12, 3.0, 0.375),   # F
    (70 - 12, 3.375, 0.375), # Ab
    (73 - 12, 3.75, 0.375),  # Bb
    (76 - 12, 4.125, 0.375), # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Return to original register, end on C
sax_notes = [
    (76, 4.5, 0.375),   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
