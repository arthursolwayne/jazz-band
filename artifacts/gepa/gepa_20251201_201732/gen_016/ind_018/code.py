
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # Gb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0), # C3

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375), # C3
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # Eb3
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125), # D3 (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5), # F2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625), # Gb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0), # C3
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0), # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0), # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0), # C5
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0), # Eb4
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5), # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5), # D5
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5), # F4
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5), # Ab4
])

# Bar 4: D7sus (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0), # D5
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0), # F5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # A5
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0), # C5
])
piano.notes.extend(piano_notes)

# Sax: one short motif, start it, leave it hanging, come back and finish it
# Motif: F (53) -> Ab (51) -> C (55), then repeat but finish with a higher F (58)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75), # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=2.0), # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.25), # C5
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.75), # F4
    pretty_midi.Note(velocity=100, pitch=51, start=2.75, end=3.0), # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25), # C5
    pretty_midi.Note(velocity=100, pitch=58, start=3.25, end=3.5), # F5
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.25), # F4
    pretty_midi.Note(velocity=100, pitch=51, start=4.25, end=4.5), # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.75), # C5
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0), # F5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
