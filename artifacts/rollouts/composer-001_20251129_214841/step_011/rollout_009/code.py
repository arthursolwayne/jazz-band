
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
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &2
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &3
    (42, 1.125, 0.1875), # Hihat on 4
    (36, 1.5, 0.375)    # Kick on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (60, 1.5, 0.375), # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375), # D
    (63, 2.625, 0.375) # D#
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.875, 0.375), # C
    (64, 1.875, 0.375), # E
    (67, 1.875, 0.375), # G
    (71, 1.875, 0.375), # Bb
    (60, 2.625, 0.375), # C
    (64, 2.625, 0.375), # E
    (67, 2.625, 0.375), # G
    (71, 2.625, 0.375)  # Bb
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (36, 2.25, 0.375),  # Kick on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 1.5, 0.1875),  # Hihat on 1
    (42, 1.6875, 0.1875), # Hihat on &1
    (42, 1.875, 0.1875), # Hihat on 2
    (42, 2.0625, 0.1875), # Hihat on &2
    (42, 2.25, 0.1875), # Hihat on 3
    (42, 2.4375, 0.1875), # Hihat on &3
    (42, 2.625, 0.1875), # Hihat on 4
    (42, 2.8125, 0.1875)  # Hihat on &4
]

for note, start, duration in drum_notes_bar2:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax - short motif, one phrase, leave it hanging
# (E, G, Bb, C) - 62, 65, 67, 60
sax_notes = [
    (62, 1.5, 0.375),
    (65, 1.875, 0.375),
    (67, 2.25, 0.375),
    (60, 2.625, 0.375)
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (64, 3.0, 0.375), # D
    (65, 3.375, 0.375), # D#
    (66, 3.75, 0.375), # E
    (67, 4.125, 0.375) # F
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.375, 0.375), # D
    (67, 3.375, 0.375), # F
    (71, 3.375, 0.375), # A
    (74, 3.375, 0.375), # C
    (64, 4.125, 0.375), # D
    (67, 4.125, 0.375), # F
    (71, 4.125, 0.375), # A
    (74, 4.125, 0.375)  # C
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375), # Snare on 2
    (36, 3.75, 0.375),  # Kick on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 3.0, 0.1875),  # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on &1
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875), # Hihat on &2
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on &3
    (42, 4.125, 0.1875), # Hihat on 4
    (42, 4.3125, 0.1875)  # Hihat on &4
]

for note, start, duration in drum_notes_bar3:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax - leave it hanging, don't resolve
sax_notes = [
    (62, 3.0, 0.375),
    (65, 3.375, 0.375),
    (67, 3.75, 0.375),
    (60, 4.125, 0.375)
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (67, 4.5, 0.375), # F
    (68, 4.875, 0.375), # F#
    (69, 5.25, 0.375), # G
    (71, 5.625, 0.375) # A
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (67, 4.875, 0.375), # F
    (71, 4.875, 0.375), # A
    (74, 4.875, 0.375), # C
    (77, 4.875, 0.375), # D
    (67, 5.625, 0.375), # F
    (71, 5.625, 0.375), # A
    (74, 5.625, 0.375), # C
    (77, 5.625, 0.375)  # D
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar4 = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875), # Hihat on &2
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on &3
    (42, 5.625, 0.1875), # Hihat on 4
    (42, 5.8125, 0.1875)  # Hihat on &4
]

for note, start, duration in drum_notes_bar4:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax - finish the motif, resolve it
sax_notes = [
    (62, 4.5, 0.375),
    (65, 4.875, 0.375),
    (67, 5.25, 0.375),
    (60, 5.625, 0.375)
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Set tempo
midi.tempo = 120 * 60  # 120 BPM

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
