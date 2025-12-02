
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (55, 1.5, 0.375),  # D
    (56, 1.875, 0.375), # Eb
    (57, 2.25, 0.375),  # E
    (59, 2.625, 0.375), # G
    (62, 3.0, 0.375),   # Bb
    (60, 3.375, 0.375), # A
    (58, 3.75, 0.375),  # Ab
    (57, 4.125, 0.375), # E
    (55, 4.5, 0.375),   # D
    (56, 4.875, 0.375), # Eb
    (57, 5.25, 0.375),  # E
    (59, 5.625, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.875, 0.1875), # D7 - D
    (52, 1.875, 0.1875), # F# (7th)
    (57, 1.875, 0.1875), # B
    (62, 1.875, 0.1875), # F (7th?)
    # Bar 3
    (57, 3.375, 0.1875), # D7 - D
    (59, 3.375, 0.1875), # F# (7th)
    (64, 3.375, 0.1875), # C
    (62, 3.375, 0.1875), # F (7th?)
    # Bar 4
    (50, 4.875, 0.1875), # D7 - D
    (52, 4.875, 0.1875), # F# (7th)
    (57, 4.875, 0.1875), # B
    (62, 4.875, 0.1875)  # F (7th?)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875))

# Sax (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D - F# - B - D (motif), then leave it hanging on B, then come back on D
sax_notes = [
    (50, 1.5, 0.375),  # D
    (52, 1.875, 0.375), # F#
    (57, 2.25, 0.375),  # B
    (50, 2.625, 0.375), # D
    (57, 3.0, 0.375),   # B (leave it hanging)
    (50, 3.75, 0.375),  # D (come back)
    (52, 4.125, 0.375), # F#
    (57, 4.5, 0.375),   # B
    (50, 4.875, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
