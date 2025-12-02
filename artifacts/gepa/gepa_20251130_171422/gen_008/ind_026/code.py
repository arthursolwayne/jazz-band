
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1& 
    (42, 0.1875, 0.1875), # Hihat on 2
    (38, 0.375, 0.375), # Snare on 3
    (42, 0.375, 0.1875), # Hihat on 3&
    (42, 0.5625, 0.1875), # Hihat on 4
    (36, 0.75, 0.375), # Kick on 4
    (42, 0.75, 0.1875), # Hihat on 4&
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Dm
bass_notes = [
    (62, 1.5, 0.375),   # F (root)
    (63, 1.875, 0.375), # F#
    (60, 2.25, 0.375),  # D
    (62, 2.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 1.875, 0.375), # C (Dm7)
    (67, 1.875, 0.375), # E
    (69, 1.875, 0.375), # G
    (71, 1.875, 0.375), # Bb
    # Bar 3 (3.0 - 4.5s)
    (64, 3.0, 0.375),   # C (Dm7)
    (67, 3.0, 0.375),   # E
    (69, 3.0, 0.375),   # G
    (71, 3.0, 0.375),   # Bb
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: Motif in Dm
sax_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    (62, 3.0, 0.375),   # D
    (64, 3.375, 0.375), # E
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375)  # C
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Dm
bass_notes = [
    (64, 3.0, 0.375),   # F#
    (65, 3.375, 0.375), # G
    (62, 3.75, 0.375),  # D
    (64, 4.125, 0.375)  # F#
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 4.5s)
    (64, 3.375, 0.375), # C (Dm7)
    (67, 3.375, 0.375), # E
    (69, 3.375, 0.375), # G
    (71, 3.375, 0.375), # Bb
    # Bar 4 (4.5 - 6.0s)
    (64, 4.5, 0.375),   # C (Dm7)
    (67, 4.5, 0.375),   # E
    (69, 4.5, 0.375),   # G
    (71, 4.5, 0.375),   # Bb
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1& 
    (42, 3.1875, 0.1875), # Hihat on 2
    (38, 3.375, 0.375), # Snare on 3
    (42, 3.375, 0.1875), # Hihat on 3&
    (42, 3.5625, 0.1875), # Hihat on 4
    (36, 3.75, 0.375), # Kick on 4
    (42, 3.75, 0.1875), # Hihat on 4&
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Dm
bass_notes = [
    (65, 4.5, 0.375),   # G
    (62, 4.875, 0.375), # D
    (64, 5.25, 0.375),  # F#
    (62, 5.625, 0.375)  # D
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 6.0s)
    (64, 4.875, 0.375), # C (Dm7)
    (67, 4.875, 0.375), # E
    (69, 4.875, 0.375), # G
    (71, 4.875, 0.375), # Bb
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1& 
    (42, 4.6875, 0.1875), # Hihat on 2
    (38, 4.875, 0.375), # Snare on 3
    (42, 4.875, 0.1875), # Hihat on 3&
    (42, 5.0625, 0.1875), # Hihat on 4
    (36, 5.25, 0.375), # Kick on 4
    (42, 5.25, 0.1875), # Hihat on 4&
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: End of motif (Bar 4)
sax_notes = [
    (62, 5.25, 0.375),  # D
    (64, 5.625, 0.375)  # E
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
