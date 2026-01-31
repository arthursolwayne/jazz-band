
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

# Marcus: Walking line (F2 - C3, MIDI 53 - 60)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # G2 on 2
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # Bb2 on 4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # B2 on 1
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75), # A2 on 2
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),  # F2 on 4
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25), # G2 on 2
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # Bb2 on 4
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=2.25),  # E
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=3.0),  # Bb (extension)
])

# Bar 4: D7 (D, F#, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.75),  # C
])

# Bar 5: F7 (F, A, C, E) - Resolving back
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.5),  # E
])

# Bar 6: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=5.25),  # Bb (extension)
])

# Bar 7: D7 (D, F#, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=6.0),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=5.25, end=6.0),  # C
])

piano.notes.extend(piano_notes)

# Dante: Tenor Sax
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (71), Bb (77), B (78), F (71) - 1.5 to 2.25
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=77, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=78, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=78, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=77, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=78, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=6.0),   # F (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375),  # Hihat on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),  # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),  # Hihat on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),  # Snare on 4
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)   # Hihat on 4
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
