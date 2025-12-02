
import pretty_midi

# Initialize MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum sounds
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray (0.0 - 1.5s)
# Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
for beat in [0, 1, 2, 3]:
    # Kick on 1 and 3 (beat 0 and 2 in bar)
    if beat in [0, 2]:
        note = pretty_midi.Note(
            velocity=100,
            pitch=KICK,
            start=beat * 0.375,
            end=(beat + 1) * 0.375
        )
        drums.notes.append(note)
    # Snare on 2 and 4 (beat 1 and 3 in bar)
    if beat in [1, 3]:
        note = pretty_midi.Note(
            velocity=90,
            pitch=SNARE,
            start=beat * 0.375,
            end=(beat + 1) * 0.375
        )
        drums.notes.append(note)
    # Hi-hat on every eighth
    note = pretty_midi.Note(
        velocity=60,
        pitch=HIHAT,
        start=beat * 0.375,
        end=(beat + 1) * 0.375
    )
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Time starts from 1.5s (bar 2)
# First bar of music (bar 2) starts at 1.5s

# Bass (Marcus): Walking line in F minor, chromatic approach
# F minor scale: F, Gb, G, Ab, A, Bb, B, C
# Walking line: F - Gb - G - Ab (chromatic approach) -> A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # Gb
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4, rootless
# F7 = A, C, E, G
# Bb7 = D, F, Ab, Bb
# C7 = E, G, B, D
# E7 = G#, B, D, F
# Chord progression: F7 - Bb7 - C7 - E7

# Bar 2 (1.5s - 3.0s)
# Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # G#
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif — F, Ab, G, F – start it, leave it hanging, return
# Bar 2: F (start), Ab (beat 2), G (beat 3), F (beat 4)
# Bar 3: F (beat 1), Ab (beat 2), G (beat 3), F (beat 4)
# Bar 4: F (beat 1), Ab (beat 2), G (beat 3), F (beat 4)

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # F (left hanging)
]

# Bar 3
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # F
])

# Bar 4
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),   # Ab
])

sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    for beat in [0, 1, 2, 3]:
        if beat in [0, 2]:
            note = pretty_midi.Note(
                velocity=100,
                pitch=KICK,
                start=bar_start + beat * 0.375,
                end=bar_start + (beat + 1) * 0.375
            )
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(
                velocity=90,
                pitch=SNARE,
                start=bar_start + beat * 0.375,
                end=bar_start + (beat + 1) * 0.375
            )
            drums.notes.append(note)
        note = pretty_midi.Note(
            velocity=60,
            pitch=HIHAT,
            start=bar_start + beat * 0.375,
            end=bar_start + (beat + 1) * 0.375
        )
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file created: 'dante_intro.mid'")
