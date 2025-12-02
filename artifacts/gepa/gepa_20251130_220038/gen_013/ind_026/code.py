
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (34, 1.5, 0.375), (36, 1.875, 0.375), (35, 2.25, 0.375), (32, 2.625, 0.375),
    (34, 3.0, 0.375), (36, 3.375, 0.375), (35, 3.75, 0.375), (32, 4.125, 0.375),
    (34, 4.5, 0.375), (36, 4.875, 0.375), (35, 5.25, 0.375), (32, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 0.1875), (63, 1.5, 0.1875), (60, 1.5, 0.1875), (61, 1.5, 0.1875),  # F7
    (64, 2.25, 0.1875), (63, 2.25, 0.1875), (60, 2.25, 0.1875), (61, 2.25, 0.1875),  # F7
    # Bar 3
    (64, 3.0, 0.1875), (63, 3.0, 0.1875), (60, 3.0, 0.1875), (61, 3.0, 0.1875),  # F7
    (64, 3.75, 0.1875), (63, 3.75, 0.1875), (60, 3.75, 0.1875), (61, 3.75, 0.1875),  # F7
    # Bar 4
    (64, 4.5, 0.1875), (63, 4.5, 0.1875), (60, 4.5, 0.1875), (61, 4.5, 0.1875),  # F7
    (64, 5.25, 0.1875), (63, 5.25, 0.1875), (60, 5.25, 0.1875), (61, 5.25, 0.1875)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Motif in Fm, one short motif, make it sing
# Motif: F, Ab, Bb, D (Fm chord tones)
sax_notes = [
    (65, 1.5, 0.375), (62, 1.875, 0.375), (62, 2.25, 0.375), (65, 2.625, 0.375),  # First pass
    (62, 3.0, 0.375), (62, 3.375, 0.375), (65, 3.75, 0.375), (62, 4.125, 0.375),  # Repeat
    (65, 4.5, 0.375), (62, 4.875, 0.375), (62, 5.25, 0.375), (65, 5.625, 0.375)   # Finish
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("waynes_intro.mid")
