
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line in Fm (F, Ab, D, C)
# Fm = F, Ab, D, C (roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),  # C2
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # C2
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),  # F2
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625), # D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),  # C2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # Eb4
    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Ab4
    # Bar 4 (C7)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Bb4
    # Bar 4 (Chordal resolution)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # Bb4
    # Bar 4 (End of phrase)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (Start of motif)
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),  # Bb4
    # Bar 3 (Leave it hanging)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),  # G4
    # Bar 4 (Come back and finish it)
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # Eb4
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=110, pitch=66, start=4.25, end=4.5),  # G4
    pretty_midi.Note(velocity=110, pitch=68, start=4.5, end=4.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Bar 2
    if bar == 2:
        kick_start = bar_start
        snare_start = bar_start + 0.75
        hihat_start = bar_start
        hihat_notes = [bar_start + i * 0.375 for i in range(4)]
    else:
        kick_start = bar_start
        snare_start = bar_start + 0.75
        hihat_start = bar_start
        hihat_notes = [bar_start + i * 0.375 for i in range(4)]

    # Kick on 1 and 3
    for kick in [kick_start, kick_start + 0.75]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick, end=kick + 0.375))

    # Snare on 2 and 4
    for snare in [snare_start, snare_start + 0.75]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare, end=snare + 0.375))

    # Hihat on every eighth
    for hihat in hihat_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat, end=hihat + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
