
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
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.125),  # Hihat on &1
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.75, 0.125),   # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.125),  # Hihat on &3
    (38, 1.5, 0.375),    # Snare on 4
    (42, 1.5, 0.125)     # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (21, 1.5, 0.375),    # F (root)
    (20, 1.875, 0.375),  # Eb (chromatic)
    (22, 2.25, 0.375),   # Gb (3rd)
    (23, 2.625, 0.375),  # Ab (4th)
    (21, 2.625, 0.375),  # F (root)
    (20, 3.0, 0.375),    # Eb (chromatic)
    (22, 3.375, 0.375),  # Gb (3rd)
    (23, 3.75, 0.375),   # Ab (4th)
    (21, 3.75, 0.375),   # F (root)
    (20, 4.125, 0.375),  # Eb (chromatic)
    (22, 4.5, 0.375),    # Gb (3rd)
    (23, 4.875, 0.375),  # Ab (4th)
    (21, 4.875, 0.375),  # F (root)
    (20, 5.25, 0.375),   # Eb (chromatic)
    (22, 5.625, 0.375),  # Gb (3rd)
    (23, 6.0, 0.375)     # Ab (4th)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (21, 2.25, 0.375),  # F7 - F
    (24, 2.25, 0.375),  # F7 - A
    (23, 2.25, 0.375),  # F7 - Ab
    (19, 2.25, 0.375),  # F7 - Eb
    # Bar 3
    (21, 3.75, 0.375),  # F7 - F
    (24, 3.75, 0.375),  # F7 - A
    (23, 3.75, 0.375),  # F7 - Ab
    (19, 3.75, 0.375),  # F7 - Eb
    # Bar 4
    (21, 5.25, 0.375),  # F7 - F
    (24, 5.25, 0.375),  # F7 - A
    (23, 5.25, 0.375),  # F7 - Ab
    (19, 5.25, 0.375)   # F7 - Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    drum_notes.append((36, bar_start, 0.375))        # Kick on 1
    drum_notes.append((42, bar_start + 0.375, 0.125)) # Hihat on &1
    drum_notes.append((38, bar_start + 0.75, 0.375))  # Snare on 2
    drum_notes.append((42, bar_start + 0.75, 0.125))  # Hihat on &2
    drum_notes.append((36, bar_start + 1.125, 0.375)) # Kick on 3
    drum_notes.append((42, bar_start + 1.125, 0.125)) # Hihat on &3
    drum_notes.append((38, bar_start + 1.5, 0.375))   # Snare on 4
    drum_notes.append((42, bar_start + 1.5, 0.125))   # Hihat on &4

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (21, 1.5, 0.75),    # F (start the motif)
    (23, 2.25, 0.75),   # Ab (continue)
    (24, 3.0, 0.75),    # A (hold)
    (21, 3.75, 0.75),   # F (come back)
    (23, 4.5, 0.75),    # Ab (finish the motif)
    (21, 5.25, 1.5)     # F (rest, leave it hanging)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
