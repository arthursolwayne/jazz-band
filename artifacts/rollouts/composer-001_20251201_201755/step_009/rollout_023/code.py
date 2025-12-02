
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25), # F
    # Bar 3: C (fifth of F) with chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # C
    # Bar 4: F (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # F
    # Bar 5: G (fifth of C) with chromatic approach from F#
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # G
    # Bar 6: F (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # F
    # Bar 7: C (fifth of F) with chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875), # E
]
# Bar 3: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625), # C
])
# Bar 4: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # F
])
# Bar 5: Cmaj7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125), # B
])
# Bar 6: F7 (F, A, C, E)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875), # E
])
# Bar 7: Cmaj7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625), # B
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, F (start), then leave it hanging on G, then come back with F, G, A
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # G (hanging)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue for Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in range(2, 7):
    start = 1.5 + (bar - 2) * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
# Hihat on every eighth
for bar in range(2, 7):
    start = 1.5 + (bar - 2) * 1.5
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
