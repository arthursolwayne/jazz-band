
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: MIDI note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Only drums (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375  # 0.375s per beat
    # Kick on beats 0 and 2 (1 and 3)
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Snare on beats 1 and 3 (2 and 4)
    if beat % 2 == 1:
        note = pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hi-hat on every eighth note
    note = pretty_midi.Note(velocity=70, pitch=HIHAT, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches, no repeated notes
# Dm7: D F A C
# Dm7 -> Gm7 -> Cm7 -> F7 -> Bb7
# Walking bass from Dm to Bb7

# Bar 2: Dm7 -> Gm7
bar_start = 1.5
bass_notes = [
    (bar_start, 50),  # D
    (bar_start + 0.375, 48),  # F
    (bar_start + 0.75, 52),  # A
    (bar_start + 1.125, 55),  # C
    (bar_start + 1.5, 57),  # E (chromatic approach to F)
    (bar_start + 1.875, 50),  # D
    (bar_start + 2.25, 52),  # A
    (bar_start + 2.625, 55),  # C
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping around you
# Dm7 on beat 2, Gm7 on beat 4
piano_notes = [
    # Bar 2
    (bar_start + 0.75, 62),  # F (7th chord: Dm7)
    (bar_start + 0.75, 64),  # A
    (bar_start + 0.75, 67),  # C
    (bar_start + 0.75, 71),  # D
    (bar_start + 1.125, 62),  # F (Dm7)
    (bar_start + 1.125, 64),  # A
    (bar_start + 1.125, 67),  # C
    (bar_start + 1.125, 71),  # D
    (bar_start + 2.25, 67),  # G (Gm7)
    (bar_start + 2.25, 71),  # Bb
    (bar_start + 2.25, 74),  # D
    (bar_start + 2.25, 77),  # F
    (bar_start + 2.625, 67),  # G
    (bar_start + 2.625, 71),  # Bb
    (bar_start + 2.625, 74),  # D
    (bar_start + 2.625, 77),  # F
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Sax: Your motif — short, singable, starts in bar 2
# Dm7: D F A C
# Motif: D -> F -> A -> C -> D (call and response)
# Notes in MIDI: D = 62, F = 64, A = 67, C = 67 (or 65?), D = 62

sax_notes = [
    (bar_start + 0.375, 62),  # D
    (bar_start + 0.75, 64),  # F
    (bar_start + 1.125, 67),  # A
    (bar_start + 1.5, 69),  # C
    (bar_start + 1.875, 64),  # F
    (bar_start + 2.25, 67),  # A
    (bar_start + 2.625, 69),  # C
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Update the MIDI file with all the instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
