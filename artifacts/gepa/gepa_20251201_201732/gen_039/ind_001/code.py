
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (bass) - Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # C2
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # C2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Diane (piano) - Open voicings, one chord per bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # D5

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0),  # F5
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),  # Ab4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # G6
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # Bb5

    # Bar 4: Resolution to Fm7
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),  # D5
]
piano.notes.extend(piano_notes)

# Dante (sax) - One short motif, make it sing
# Motif: F, Ab, Bb, F (Fm6)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))  # Hihat
    # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125))  # Hihat
    # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5))  # Hihat
    # Snare on 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875))  # Hihat

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
