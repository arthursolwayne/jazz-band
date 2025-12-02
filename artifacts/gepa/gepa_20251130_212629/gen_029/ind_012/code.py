
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
    (42, 0.1875, 0.1875), # Hihat on &1
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &2
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &3
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &4
    (36, 1.5, 0.375)    # Kick on 3
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in Fm
bass_notes = [
    (39, 1.5, 0.375), # F (39) on 1
    (40, 1.875, 0.375), # Gb (40) on 2
    (41, 2.25, 0.375), # Ab (41) on 3
    (43, 2.625, 0.375), # Bb (43) on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on 2 (1.875)
    (45, 1.875, 0.375), # F (45)
    (48, 1.875, 0.375), # Ab (48)
    (50, 1.875, 0.375), # C (50)
    (51, 1.875, 0.375), # Db (51)
    
    # Fm7 on 4 (2.625)
    (45, 2.625, 0.375), # F
    (48, 2.625, 0.375), # Ab
    (50, 2.625, 0.375), # C
    (51, 2.625, 0.375), # Db
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.5, 0.1875), # Hihat on 1
    (42, 1.6875, 0.1875), # Hihat on &1
    (42, 1.875, 0.1875), # Hihat on 2
    (42, 2.0625, 0.1875), # Hihat on &2
    (42, 2.25, 0.1875), # Hihat on 3
    (42, 2.4375, 0.1875), # Hihat on &3
    (42, 2.625, 0.1875), # Hihat on 4
    (42, 2.8125, 0.1875), # Hihat on &4
    (36, 2.25, 0.375)    # Kick on 3
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line in Fm
bass_notes = [
    (43, 3.0, 0.375), # Bb on 1
    (45, 3.375, 0.375), # F on 2
    (47, 3.75, 0.375), # G on 3
    (48, 4.125, 0.375), # Ab on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on 2 (3.375)
    (45, 3.375, 0.375), # F
    (48, 3.375, 0.375), # Ab
    (50, 3.375, 0.375), # C
    (51, 3.375, 0.375), # Db

    # Fm7 on 4 (4.125)
    (45, 4.125, 0.375), # F
    (48, 4.125, 0.375), # Ab
    (50, 4.125, 0.375), # C
    (51, 4.125, 0.375), # Db
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.0, 0.1875), # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on &1
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875), # Hihat on &2
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on &3
    (42, 4.125, 0.1875), # Hihat on 4
    (42, 4.3125, 0.1875), # Hihat on &4
    (36, 3.75, 0.375)    # Kick on 3
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line in Fm
bass_notes = [
    (48, 4.5, 0.375), # Ab on 1
    (45, 4.875, 0.375), # F on 2
    (47, 5.25, 0.375), # G on 3
    (50, 5.625, 0.375), # C on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on 2 (4.875)
    (45, 4.875, 0.375), # F
    (48, 4.875, 0.375), # Ab
    (50, 4.875, 0.375), # C
    (51, 4.875, 0.375), # Db

    # Fm7 on 4 (5.625)
    (45, 5.625, 0.375), # F
    (48, 5.625, 0.375), # Ab
    (50, 5.625, 0.375), # C
    (51, 5.625, 0.375), # Db
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875), # Hihat on &2
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on &3
    (42, 5.625, 0.1875), # Hihat on 4
    (42, 5.8125, 0.1875), # Hihat on &4
    (36, 5.25, 0.375)    # Kick on 3
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone: Short motif, starts on 1.5s, ends on 4.0s
sax_notes = [
    # Bar 2: sax starts on 1.5s (beat 1 of bar 2)
    (43, 1.5, 0.375), # Bb
    (42, 1.875, 0.375), # Ab
    (40, 2.25, 0.375), # Gb
    (45, 2.625, 0.375), # F
    (43, 3.0, 0.1875), # Bb
    (41, 3.1875, 0.1875), # Ab
    (40, 3.375, 0.1875), # Gb
    (45, 3.5625, 0.1875), # F
    (43, 3.75, 0.1875), # Bb
    (42, 3.9375, 0.1875), # Ab
    (40, 4.125, 0.1875), # Gb
    (45, 4.3125, 0.1875), # F
    (43, 4.5, 0.375), # Bb
    (42, 4.875, 0.375), # Ab
    (40, 5.25, 0.375), # Gb
    (45, 5.625, 0.375), # F
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add dynamics to saxophone
for note in sax.notes:
    if note.start >= 1.5 and note.start < 3.0:
        note.velocity = 110  # Stronger in first half
    else:
        note.velocity = 100  # Softer in the second half

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
