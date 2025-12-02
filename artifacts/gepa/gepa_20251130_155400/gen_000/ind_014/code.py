
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
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4 (1.5 - 6.0s)
# Bass: Walking line in Fm with chromatic approaches
bass_notes = [
    (36, 1.5, 0.375),  # F
    (37, 1.875, 0.375), # Gb
    (35, 2.25, 0.375),  # E
    (34, 2.625, 0.375), # D
    (36, 3.0, 0.375),   # F
    (37, 3.375, 0.375), # Gb
    (35, 3.75, 0.375),  # E
    (34, 4.125, 0.375), # D
    (36, 4.5, 0.375),   # F
    (37, 4.875, 0.375), # Gb
    (35, 5.25, 0.375),  # E
    (34, 5.625, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (45, 2.25, 0.1875), # Bb
    (48, 2.25, 0.1875), # D
    (49, 2.25, 0.1875), # Eb
    (53, 2.25, 0.1875), # A
    (45, 2.625, 0.1875),
    (48, 2.625, 0.1875),
    (49, 2.625, 0.1875),
    (53, 2.625, 0.1875),
    
    # Bar 3: F7 on 2 and 4
    (45, 3.75, 0.1875),
    (48, 3.75, 0.1875),
    (49, 3.75, 0.1875),
    (53, 3.75, 0.1875),
    (45, 4.125, 0.1875),
    (48, 4.125, 0.1875),
    (49, 4.125, 0.1875),
    (53, 4.125, 0.1875),
    
    # Bar 4: F7 on 2 and 4
    (45, 5.25, 0.1875),
    (48, 5.25, 0.1875),
    (49, 5.25, 0.1875),
    (53, 5.25, 0.1875),
    (45, 5.625, 0.1875),
    (48, 5.625, 0.1875),
    (49, 5.625, 0.1875),
    (53, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif - F, Ab, G, F (start on bar 2)
sax_notes = [
    (53, 2.0, 0.1875), # F
    (55, 2.375, 0.1875), # Ab
    (54, 2.75, 0.1875), # G
    (53, 3.125, 0.1875)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes = [
        (36, bar_start, 0.375), (38, bar_start + 0.375, 0.375), (42, bar_start, 0.1875),
        (36, bar_start + 0.75, 0.375), (38, bar_start + 1.125, 0.375), (42, bar_start + 0.75, 0.1875),
        (36, bar_start + 1.5, 0.375), (38, bar_start + 1.875, 0.375), (42, bar_start + 1.5, 0.1875),
        (36, bar_start + 2.25, 0.375), (38, bar_start + 2.625, 0.375), (42, bar_start + 2.25, 0.1875)
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
