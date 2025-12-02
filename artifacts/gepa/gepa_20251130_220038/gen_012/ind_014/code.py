
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
    (36, 1.5, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Everyone in. Sax takes the melody (1.5 - 3.0s)
# Fm key, one short motif. Start it, leave it hanging. Make it sing.
# Fm7 = F Ab C Eb
# Motif: F Ab C Eb (F, Ab, C, Eb) - descending, chromatic approach

# Sax
sax_notes = [
    (84, 1.5, 0.375),  # F
    (80, 1.875, 0.375),  # Ab
    (87, 2.25, 0.375),  # C
    (83, 2.625, 0.375),  # Eb
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
# F Ab G Bb C B Eb D F
bass_notes = [
    (53, 1.5, 0.375),  # F
    (50, 1.875, 0.375),  # Ab
    (49, 2.25, 0.375),  # G
    (51, 2.625, 0.375),  # Bb
    (55, 3.0, 0.375),  # C
    (54, 3.375, 0.375),  # B
    (50, 3.75, 0.375),  # Eb
    (49, 4.125, 0.375),  # D
    (53, 4.5, 0.375),  # F
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Fm7 on 2, Bm7b5 on 4
piano_notes = [
    # Fm7 on 2
    (53, 1.875, 0.375),  # F
    (50, 1.875, 0.375),  # Ab
    (55, 1.875, 0.375),  # C
    (51, 1.875, 0.375),  # Eb

    # Bm7b5 on 4
    (62, 2.625, 0.375),  # B
    (58, 2.625, 0.375),  # D
    (64, 2.625, 0.375),  # F#
    (60, 2.625, 0.375),  # A
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Everyone in again (3.0 - 4.5s)
# Sax: Repeat the motif but with a slight variation, maybe a trill on the last note
# F Ab C Eb (trill on Eb)
sax_notes = [
    (84, 3.0, 0.375),  # F
    (80, 3.375, 0.375),  # Ab
    (87, 3.75, 0.375),  # C
    (83, 4.125, 0.375),  # Eb
    (83, 4.125, 0.1875),  # Eb
    (84, 4.3125, 0.1875),  # F
    (83, 4.5, 0.1875),  # Eb
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line again
bass_notes = [
    (53, 3.0, 0.375),  # F
    (50, 3.375, 0.375),  # Ab
    (49, 3.75, 0.375),  # G
    (51, 4.125, 0.375),  # Bb
    (55, 4.5, 0.375),  # C
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on 2
    (53, 3.375, 0.375),  # F
    (50, 3.375, 0.375),  # Ab
    (55, 3.375, 0.375),  # C
    (51, 3.375, 0.375),  # Eb

    # Bm7b5 on 4
    (62, 4.125, 0.375),  # B
    (58, 4.125, 0.375),  # D
    (64, 4.125, 0.375),  # F#
    (60, 4.125, 0.375),  # A
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.75, 0.375),  # Snare on 2
    (42, 3.0, 0.1875),  # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on &1
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875), # Hihat on &2
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on &3
    (42, 4.125, 0.1875), # Hihat on 4
    (42, 4.3125, 0.1875), # Hihat on &4
    (36, 4.5, 0.375),  # Kick on 3
    (38, 4.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Everyone in again (4.5 - 6.0s)
# Sax: Bring back the motif and resolve it
# F Ab C Eb -> F
sax_notes = [
    (84, 4.5, 0.375),  # F
    (80, 4.875, 0.375),  # Ab
    (87, 5.25, 0.375),  # C
    (83, 5.625, 0.375),  # Eb
    (84, 6.0, 0.375),  # F
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line again
bass_notes = [
    (53, 4.5, 0.375),  # F
    (50, 4.875, 0.375),  # Ab
    (49, 5.25, 0.375),  # G
    (51, 5.625, 0.375),  # Bb
    (55, 6.0, 0.375),  # C
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on 2
    (53, 4.875, 0.375),  # F
    (50, 4.875, 0.375),  # Ab
    (55, 4.875, 0.375),  # C
    (51, 4.875, 0.375),  # Eb

    # Bm7b5 on 4
    (62, 5.625, 0.375),  # B
    (58, 5.625, 0.375),  # D
    (64, 5.625, 0.375),  # F#
    (60, 5.625, 0.375),  # A
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 5.25, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875), # Hihat on &2
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on &3
    (42, 5.625, 0.1875), # Hihat on 4
    (42, 5.8125, 0.1875), # Hihat on &4
    (36, 6.0, 0.375),  # Kick on 3
    (38, 6.0, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.dump()
