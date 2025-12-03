
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
    # Bar 1: 0.0 - 1.5s
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
# D2 (MIDI 38) to G2 (MIDI 43), with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # Ab2 (chromatic approach)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # Eb2 (chromatic approach)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),  # Ab2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # A4 (D7 chord: D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # D5
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # G5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # C#6

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # A4 (Bm7b5: B, D, F, A)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # F#5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # A5

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # A4 (Gm7: G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875), # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (MIDI 62) to D5 (MIDI 72) with syncopation and space
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # D5
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
